import time

# SORT USING MERGE SORT
def merge_sort(arr, first, last, time_limit, start_time):
    # CHECK TIME
    if time.time() - start_time >= time_limit:
        return "DNF"

    # STOP AT ONE ELEMENT
    if first >= last:
        return None

    # FIND MIDDLE
    mid = (first + last) // 2

    # SORT LEFT HALF
    result = merge_sort(
        arr,
        first,
        mid,
        time_limit,
        start_time
    )

    if result == "DNF":
        return "DNF"

    # SORT RIGHT HALF
    result = merge_sort(
        arr,
        mid + 1,
        last,
        time_limit,
        start_time
    )

    if result == "DNF":
        return "DNF"

    # MERGE HALVES
    merge(arr, first, mid, last)

    return None


# MERGE TWO HALVES
def merge(arr, first, mid, last):
    # COPY LEFT HALF
    left_half = arr[first:mid + 1]

    # COPY RIGHT HALF
    right_half = arr[mid + 1:last + 1]

    # SET POINTERS
    i = 0
    j = 0
    k = first

    # COMPARE VALUES
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1

        k += 1

    # COPY LEFT REMAINDER
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    # COPY RIGHT REMAINDER
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1