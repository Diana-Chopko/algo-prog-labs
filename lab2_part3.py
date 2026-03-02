def find_board_size(n, w, h):
    """
    Calculates the minimum side length of a square board that can fit N
    rectangular sheets of size W x H.

    :param n: The number of sheets to be placed.
    :param w: The width of a single sheet.
    :param h: The height of a single sheet.

    :return: result
    :raises: ValueError: If any of the input values (n, w, h) are less
             than or equal to zero.
    """
    if n <= 0 or w <= 0 or h <= 0:
        raise ValueError("All input values must be greater than 0")
    min_len = 1
    max_len = max(w, h) * n
    result = max_len

    while min_len <= max_len:
        mid_len = (min_len + max_len) // 2

        if mid_len == 0:
            min_len = 1
            continue

        count_sheet = (mid_len // w) * (mid_len // h)
        if count_sheet >= n:
            result = mid_len
            max_len = mid_len - 1
        else:
            min_len = mid_len + 1

    return result
