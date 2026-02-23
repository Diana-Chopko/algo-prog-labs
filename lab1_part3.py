def finding_unsorted_subarray(arr):
    """
    Finds the starting and ending indices of the shortest continuous subarray
    that needs to be sorted in order for the entire array to be sorted.

    :param arr: array, that is needed to explore if it has unsorted part or not.

    :return: index of unsorted array or (-1, -1) if the array is already
            completely sorted or contains fewer than 2 elements.
    """
    n = len(arr)
    result = (-1, -1)

    if n >= 2:
        first_el = 0
        while first_el < n - 1 and arr[first_el] <= arr[first_el + 1]:
            first_el += 1

        if first_el < n - 1:
            last_el = n - 1
            while last_el > 0 and arr[last_el] >= arr[last_el - 1]:
                last_el -= 1

            subarray_min = arr[first_el]
            subarray_max = arr[first_el]

            for i in range(first_el + 1, last_el + 1):
                if arr[i] < subarray_min:
                    subarray_min = arr[i]
                if arr[i] > subarray_max:
                    subarray_max = arr[i]

            while first_el > 0 and arr[first_el - 1] > subarray_min:
                first_el -= 1

            while last_el < n - 1 and arr[last_el + 1] < subarray_max:
                last_el += 1

            result = (first_el, last_el)

    return result
