import sys
import time

# SORT USING QUICKSORT
def quicksort(arr, first, last, time_limit, start_time, rec_limit=0):
    # CHECK TIME
    if time.time() - start_time >= time_limit:
        return "DNF"

    # CHECK RECURSION
    if rec_limit >= sys.getrecursionlimit() * 0.9:
        return "DNF-rec limit"

    # STOP AT ONE ELEMENT
    if first >= last:
        return None

    # CHOOSE MIDDLE PIVOT
    pivot = arr[(first + last) // 2]

    # SET POINTERS
    i = first
    j = last

    # PARTITION ARRAY
    while i <= j:
        # CHECK TIME
        if time.time() - start_time >= time_limit:
            return "DNF"

        # MOVE LEFT POINTER
        while arr[i] < pivot:
            i += 1

        # MOVE RIGHT POINTER
        while arr[j] > pivot:
            j -= 1

        # SWAP VALUES
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    # SORT LEFT PART
    if first < j:
        result = quicksort(
            arr,
            first,
            j,
            time_limit,
            start_time,
            rec_limit + 1
        )

        if result in ["DNF", "DNF-rec limit"]:
            return result

    # SORT RIGHT PART
    if i < last:
        result = quicksort(
            arr,
            i,
            last,
            time_limit,
            start_time,
            rec_limit + 1
        )

        if result in ["DNF", "DNF-rec limit"]:
            return result

    return None