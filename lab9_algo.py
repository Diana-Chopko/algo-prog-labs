def compute_lps(needle):
    """
    Calculates the array of longest prefixes, which are suffixes(LPS).
    :param needle: ribbon sought
    :return: lps
    """
    length = 0
    lps = [0] * len(needle)
    i = 1

    while i < len(needle):
        if needle[i] == needle[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(haystack, needle):
    """
    Finds all needle entry indices in haystack using KMP.
    :param haystack: arbitrary text
    :param needle: ribbon sought
    :return: found_indices
    """
    found_indices = []

    if not needle:
        return found_indices

    n = len(haystack)
    m = len(needle)
    lps = compute_lps(needle)

    ind_n = 0
    ind_m = 0

    while ind_n < n:
        if needle[ind_m] == haystack[ind_n]:
            ind_n += 1
            ind_m += 1

        if ind_m == m:
            found_indices.append(ind_n - ind_m)
            ind_m = lps[ind_m - 1]

        elif ind_n < n and haystack[ind_n] != needle[ind_m]:
            if ind_m != 0:
                ind_m = lps[ind_m - 1]
            else:
                ind_n += 1

    return found_indices
