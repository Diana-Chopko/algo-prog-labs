import itertools


def valid_inputs(n, b, pref_str):
    """
    Validates the input parameters. Ensures n and b are within range (0-50)
    and the preference string length matches n*b.
    :param n: number of employees.
    :param b: number of beer type.
    :param pref_str: a person's choice regarding beer types.
    :return: is_valid, error_message
    """
    is_valid = True
    error_message = ""

    if n <= 0 or n >= 50:
        is_valid = False
        error_message = "The number of employees should be 0-50."
    elif b <= 0 or b >= 50:
        is_valid = False
        error_message = "The number of beer types should be 0-50."
    elif len(pref_str) != (n * b):
        is_valid = False
        error_message = "The length of the line does not correspond to n*b."

    return is_valid, error_message


def parse_pref(n, b, pref_str):
    """
    Converts a flat preference string into a 2D matrix (list of lists).
    Each row represents an employee's preferences for each beer type.
    :param n: number of employees.
    :param b: number of beer type.
    :param pref_str: a person's choice regarding beer types.
    :return: pref_matrix
    """
    pref_matrix = []
    for i in range(n):
        emp_row = []
        for j in range(b):
            index = i * b + j
            emp_row.append(pref_str[index])
        pref_matrix.append(emp_row)

    return pref_matrix


def check_emp_like(pref_matrix):
    """
    Checks if every employee likes at least one type of beer.
    Returns False if any employee has no 'Y' preferences.
    :param pref_matrix: is a two-dimensional list
    :return: is_valid
    """
    is_valid = True

    for row in pref_matrix:
        emp_likes_beer = False
        for char in row:
            if char == "Y":
                emp_likes_beer = True
                break

        if not emp_likes_beer:
            is_valid = False
            break

    return is_valid


def calculate_min_beers(n, b, pref_matrix):
    """
    Finds the minimum number of beer types needed to satisfy all employees.
    Uses itertools.combinations to exhaustively check sets of size 1, 2 ... b.
    :param n: number of employees.
    :param b: number of beer type.
    :param pref_matrix: is a two-dimensional list.
    :return: min_beers
    """
    min_beers = b
    is_optimal = False
    current_combination = 1

    while current_combination <= b and not is_optimal:
        all_combinations = itertools.combinations(range(b), current_combination)

        for combination in all_combinations:
            all_emp_satisfied = True

            for emp_index in range(n):
                is_emp_satisfied = False

                for beer_index in combination:
                    if pref_matrix[emp_index][beer_index] == "Y":
                        is_emp_satisfied = True
                        break

                if not is_emp_satisfied:
                    all_emp_satisfied = False
                    break

            if all_emp_satisfied:
                min_beers = current_combination
                is_optimal = True
                break

        current_combination += 1

    return min_beers


def solve_beer_problem(n, b, pref_str):
    """
    The main entry point for solving the problem.
    Coordinates validation, parsing, logic checks, and calculation.
    :param n: number of employees.
    :param b: number of beer type.
    :param pref_str: a person's choice regarding beer types.
    :return: final_result
    """
    final_result = -1
    is_valid, error_message = valid_inputs(n, b, pref_str)

    if not is_valid:
        print(error_message)
    else:
        pref_matrix = parse_pref(n, b, pref_str)
        if not check_emp_like(pref_matrix):
            print("Every employee should like at least 1 type of beer.")
        else:
            final_result = calculate_min_beers(n, b, pref_matrix)

    return final_result
