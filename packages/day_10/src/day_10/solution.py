import re
from fractions import Fraction
from itertools import product


def parse_machine(line: str) -> tuple[list[int], list[list[int]]]:
    """Parse a machine line into target state and button configurations."""
    # Extract indicator lights pattern
    match = re.match(r"\[([.#]+)\]", line)
    if not match:
        msg = f"Could not parse indicator lights from: {line}"
        raise ValueError(msg)

    pattern = match.group(1)
    target = [1 if c == "#" else 0 for c in pattern]
    n_lights = len(target)

    # Extract button configurations
    buttons = []
    for m in re.finditer(r"\(([0-9,]+)\)", line):
        indices = [int(x) for x in m.group(1).split(",")]
        # Create a bitmask for which lights this button toggles
        button = [0] * n_lights
        for idx in indices:
            if idx < n_lights:
                button[idx] = 1
        buttons.append(button)

    return target, buttons


def parse_machine_part2(line: str) -> tuple[list[int], list[list[int]]]:
    """Parse a machine line for Part 2: joltage requirements and button configurations."""
    # Extract joltage requirements
    joltage_match = re.search(r"\{([0-9,]+)\}", line)
    if not joltage_match:
        msg = f"Could not parse joltage requirements from: {line}"
        raise ValueError(msg)

    target = [int(x) for x in joltage_match.group(1).split(",")]
    n_counters = len(target)

    # Extract button configurations
    buttons = []
    for m in re.finditer(r"\(([0-9,]+)\)", line):
        indices = [int(x) for x in m.group(1).split(",")]
        # Create a vector for which counters this button affects
        button = [0] * n_counters
        for idx in indices:
            if idx < n_counters:
                button[idx] = 1
        buttons.append(button)

    return target, buttons


def solve_machine_brute_force(target: list[int], buttons: list[list[int]]) -> int:
    """
    Find minimum button presses using brute force for small cases.
    Since pressing a button twice cancels out, we only need to try 0 or 1 presses.
    """
    n_buttons = len(buttons)
    n_lights = len(target)
    min_presses = n_buttons + 1  # More than maximum possible

    # Try all 2^n combinations of button presses
    for combo in product([0, 1], repeat=n_buttons):
        # Calculate the resulting light state
        state = [0] * n_lights
        for i, pressed in enumerate(combo):
            if pressed:
                for j in range(n_lights):
                    state[j] ^= buttons[i][j]

        # Check if this matches the target
        if state == target:
            presses = sum(combo)
            min_presses = min(min_presses, presses)

    return min_presses if min_presses <= n_buttons else -1


def gaussian_elimination_gf2(
    matrix: list[list[int]], target: list[int]
) -> list[list[int]] | None:
    """
    Perform Gaussian elimination over GF(2) to find all solutions.
    Returns the particular solution and null space basis vectors, or None if no solution.
    """
    n_rows = len(matrix)
    if n_rows == 0:
        return [] if all(t == 0 for t in target) else None

    n_cols = len(matrix[0])

    # Create augmented matrix [A | b]
    aug = [row[:] + [target[i]] for i, row in enumerate(matrix)]

    # Forward elimination
    pivot_cols = []
    row = 0
    for col in range(n_cols):
        # Find pivot
        pivot = None
        for r in range(row, n_rows):
            if aug[r][col] == 1:
                pivot = r
                break

        if pivot is None:
            continue

        pivot_cols.append(col)
        # Swap rows
        aug[row], aug[pivot] = aug[pivot], aug[row]

        # Eliminate below
        for r in range(n_rows):
            if r != row and aug[r][col] == 1:
                for c in range(n_cols + 1):
                    aug[r][c] ^= aug[row][c]

        row += 1

    # Check for inconsistency
    for r in range(row, n_rows):
        if aug[r][n_cols] == 1:
            return None  # No solution

    # Find particular solution
    particular = [0] * n_cols
    for i, col in enumerate(pivot_cols):
        particular[col] = aug[i][n_cols]

    # Find null space basis
    free_cols = [c for c in range(n_cols) if c not in pivot_cols]
    null_basis = []

    for free_col in free_cols:
        null_vec = [0] * n_cols
        null_vec[free_col] = 1
        for i, pivot_col in enumerate(pivot_cols):
            null_vec[pivot_col] = aug[i][free_col]
        null_basis.append(null_vec)

    return [particular] + null_basis


def min_weight_solution(solutions_data: list[list[int]]) -> int:
    """
    Find the minimum Hamming weight solution given particular solution and null basis.
    """
    if not solutions_data:
        return 0

    particular = solutions_data[0]
    null_basis = solutions_data[1:]

    if not null_basis:
        return sum(particular)

    # Try all combinations of null space vectors
    n_null = len(null_basis)
    n_vars = len(particular)
    min_weight = sum(particular)

    for combo in product([0, 1], repeat=n_null):
        solution = particular[:]
        for i, use in enumerate(combo):
            if use:
                for j in range(n_vars):
                    solution[j] ^= null_basis[i][j]
        weight = sum(solution)
        min_weight = min(min_weight, weight)

    return min_weight


def solve_machine(target: list[int], buttons: list[list[int]]) -> int:
    """
    Find minimum button presses to reach target state.
    Uses Gaussian elimination over GF(2).
    """
    if not buttons:
        return 0 if all(t == 0 for t in target) else -1

    n_lights = len(target)
    n_buttons = len(buttons)

    # For small cases, use brute force (more reliable)
    if n_buttons <= 20:
        return solve_machine_brute_force(target, buttons)

    # Build matrix where each column is a button's effect on lights
    # We want to solve: sum of (x_i * button_i) = target (mod 2)
    # This is Ax = b where A is n_lights x n_buttons

    matrix = [[buttons[j][i] for j in range(n_buttons)] for i in range(n_lights)]

    solutions = gaussian_elimination_gf2(matrix, target)
    if solutions is None:
        return -1

    return min_weight_solution(solutions)


def solve_part1(input_data: str) -> int:
    lines = input_data.strip().split("\n")
    total = 0

    for line in lines:
        target, buttons = parse_machine(line)
        presses = solve_machine(target, buttons)
        if presses == -1:
            msg = f"No solution found for: {line}"
            raise ValueError(msg)
        total += presses

    return total


def solve_ilp_machine(target: list[int], buttons: list[list[int]]) -> int:
    """
    Solve the integer linear programming problem for Part 2.
    Find non-negative integers x_i such that sum(x_i * button_i) = target,
    minimizing sum(x_i).

    Uses Gaussian elimination to find the solution space, then searches
    for the minimum sum solution with non-negative integers.
    """
    n_buttons = len(buttons)
    n_counters = len(target)

    if n_buttons == 0:
        return 0 if all(t == 0 for t in target) else -1

    # Build matrix A where A[i][j] = 1 if button j affects counter i
    # We want to solve Ax = b where x >= 0 and x is integer
    matrix = [[buttons[j][i] for j in range(n_buttons)] for i in range(n_counters)]

    # Perform Gaussian elimination to get RREF
    aug: list[list[Fraction]] = [
        [Fraction(x) for x in row] + [Fraction(target[i])]
        for i, row in enumerate(matrix)
    ]

    n_rows = n_counters
    n_cols = n_buttons

    pivot_cols = []
    pivot_rows: dict[int, int] = {}  # col -> row
    row = 0
    for col in range(n_cols):
        # Find pivot
        pivot = None
        for r in range(row, n_rows):
            if aug[r][col] != 0:
                pivot = r
                break

        if pivot is None:
            continue

        pivot_cols.append(col)
        pivot_rows[col] = row
        # Swap rows
        aug[row], aug[pivot] = aug[pivot], aug[row]

        # Scale pivot row
        scale = aug[row][col]
        for c in range(n_cols + 1):
            aug[row][c] /= scale

        # Eliminate other rows
        for r in range(n_rows):
            if r != row and aug[r][col] != 0:
                factor = aug[r][col]
                for c in range(n_cols + 1):
                    aug[r][c] -= factor * aug[row][c]

        row += 1

    # Check for inconsistency
    for r in range(row, n_rows):
        if aug[r][n_cols] != 0:
            return -1  # No solution

    free_cols = [c for c in range(n_cols) if c not in pivot_cols]

    # If no free variables, we have a unique solution
    if not free_cols:
        solution = [Fraction(0)] * n_cols
        for col in pivot_cols:
            r = pivot_rows[col]
            solution[col] = aug[r][n_cols]
        # Check if solution is non-negative integer
        for val in solution:
            if val < 0 or val.denominator != 1:
                return -1
        return sum(int(val) for val in solution)

    # We have free variables - need to search for minimum sum non-negative integer solution
    # Each pivot variable is expressed in terms of free variables:
    # x_pivot = constant - sum(coeff * x_free)

    # Express pivot variables in terms of free variables
    constants: dict[int, Fraction] = {}
    coeffs: dict[int, dict[int, Fraction]] = {}
    for col in pivot_cols:
        r = pivot_rows[col]
        constants[col] = aug[r][n_cols]
        coeffs[col] = {fc: aug[r][fc] for fc in free_cols}

    # Find bounds for free variables
    max_target = max(target) if target else 0

    def evaluate_solution(free_vals: list[int]) -> int | None:
        """Given free variable values, compute total if valid, else None."""
        total = sum(free_vals)
        for col in pivot_cols:
            val = constants[col]
            for i, fc in enumerate(free_cols):
                val -= coeffs[col][fc] * free_vals[i]
            if val < 0 or val.denominator != 1:
                return None
            total += int(val)
        return total

    # Compute a generous upper bound for free variables
    # The maximum needed is roughly max(target) plus compensation for negative constants
    max_neg_const = max(
        (-int(constants[c]) for c in pivot_cols if constants[c] < 0), default=0
    )
    generous_upper = max(max_target, max_neg_const) + 10

    min_sum: int | None = None
    n_free = len(free_cols)

    def get_bounds(free_idx: int, free_vals: list[int]) -> tuple[int, int]:
        """Compute lower and upper bounds for free variable at free_idx."""
        fc = free_cols[free_idx]
        lower = 0
        upper = generous_upper
        remaining_free = free_cols[free_idx + 1 :]

        for col in pivot_cols:
            coeff = coeffs[col][fc]
            # Current remaining constant
            remaining = constants[col]
            for i, prev_fc in enumerate(free_cols[:free_idx]):
                remaining -= coeffs[col][prev_fc] * free_vals[i]

            if coeff < 0:
                # x_pivot = remaining + |coeff| * x_fc >= 0
                if remaining < 0:
                    # Need x_fc to compensate, unless later vars can help
                    can_help = any(coeffs[col][rfc] < 0 for rfc in remaining_free)
                    if not can_help:
                        needed = int((-remaining + (-coeff) - 1) / (-coeff))
                        lower = max(lower, needed)
            elif coeff > 0:
                # x_pivot = remaining - coeff * x_fc + sum(-c_rfc * x_rfc) >= 0
                # A later var with negative coeff can ADD to x_pivot, offsetting x_fc
                can_help = any(coeffs[col][rfc] < 0 for rfc in remaining_free)
                if remaining >= 0:
                    if not can_help:
                        upper = min(upper, int(remaining / coeff))
                elif not can_help:
                    return (1, 0)  # Infeasible

        return (lower, upper)

    def search(free_idx: int, free_vals: list[int], current_sum: int) -> None:
        nonlocal min_sum

        if min_sum is not None and current_sum >= min_sum:
            return

        if free_idx == n_free:
            result = evaluate_solution(free_vals)
            if result is not None and (min_sum is None or result < min_sum):
                min_sum = result
            return

        lower, upper = get_bounds(free_idx, free_vals)
        if lower > upper:
            return

        for val in range(lower, upper + 1):
            if min_sum is not None and current_sum + val >= min_sum:
                break
            free_vals.append(val)
            search(free_idx + 1, free_vals, current_sum + val)
            free_vals.pop()

    search(0, [], 0)

    return min_sum if min_sum is not None else -1


def solve_part2(input_data: str) -> int:
    lines = input_data.strip().split("\n")
    total = 0

    for line in lines:
        target, buttons = parse_machine_part2(line)
        presses = solve_ilp_machine(target, buttons)
        if presses == -1:
            msg = f"No solution found for: {line}"
            raise ValueError(msg)
        total += presses

    return total
