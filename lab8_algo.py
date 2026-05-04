import math


def check_data(w, heights):
    """
    Validates the input data according to the given constraints.
    :param w: The horizontal distance between the poles.
    :param heights: A list of maximum possible heights for each pole.
    :return: is_valid
    """
    is_valid = True

    if type(w) is not int or w < 1 or w > 100:
        is_valid = False

    n = len(heights)
    if n < 2 or n > 50:
        is_valid = False

    for h in heights:
        if type(h) is not int or h < 1 or h > 100:
            is_valid = False

    return is_valid


def calculate_distance(w, h1, h2):
    """
    Calculates the wire length between the tops of two adjacent poles.
    :param w: The horizontal distance between the poles.
    :param h1: The height of the previous pole.
    :param h2: The height of the current pole.
    :return: distance
    """
    distance = math.sqrt(w ** 2 + (h1 - h2) ** 2)
    return distance


def max_wire_len(w, height):
    """
    Calculates the maximum possible total length of the wire using dynamic
    programming. It assumes each pole can be either height 1 or its maximum
    possible height.
    :param w: The horizontal distance between the poles.
    :param height: A list of maximum possible heights for each pole.
    :return: final_result
    """
    if not check_data(w, height):
        final_result = "Error. Please check the data."
    else:
        n = len(height)
        dp_1 = 0.0
        dp_max = 0.0

        for i in range(1, n):
            prev_h_1 = 1
            prev_h_max = height[i - 1]

            curr_h_1 = 1
            curr_h_max = height[i]

            dist_1_to_1 = calculate_distance(w, prev_h_1, curr_h_1)
            dist_max_to_1 = calculate_distance(w, prev_h_max, curr_h_1)
            new_dp_1 = max(dp_1 + dist_1_to_1, dp_max + dist_max_to_1)

            dist_1_to_max = calculate_distance(w, prev_h_1, curr_h_max)
            dist_max_to_max = calculate_distance(w, prev_h_max, curr_h_max)
            new_dp_max = max(dp_1 + dist_1_to_max, dp_max + dist_max_to_max)

            dp_1 = new_dp_1
            dp_max = new_dp_max

        result = max(dp_1, dp_max)
        final_result = round(result, 2)

    return final_result
