import time

# SORT USING BUBBLE SORT
def bubble_sort(arr, time_limit, start_time):
    # SET ARRAY SIZE
    n = len(arr)

    # REPEAT PASSES
    while n > 1:
        # CHECK TIME
        if time.time() - start_time >= time_limit:
            return "DNF"

        # TRACK SWAPS
        swapped = False

        # COMPARE NEIGHBOURS
        for i in range(n - 1):
            # CHECK TIME
            if time.time() - start_time >= time_limit:
                return "DNF"

            # SWAP IF NEEDED
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # STOP IF SORTED
        if not swapped:
            break

        # IGNORE LAST SORTED VALUE
        n -= 1

    return None