import time

# SORT USING INSERTION SORT
def insertion_sort(arr, time_limit, start_time):
    # LOOP THROUGH ARRAY
    for i in range(1, len(arr)):
        # CHECK TIME
        if time.time() - start_time >= time_limit:
            return "DNF"

        # SAVE CURRENT VALUE
        value = arr[i]

        # START FROM PREVIOUS VALUE
        j = i - 1

        # MOVE LARGER VALUES
        while j >= 0 and arr[j] > value:
            # CHECK TIME
            if time.time() - start_time >= time_limit:
                return "DNF"

            arr[j + 1] = arr[j]
            j -= 1

        # INSERT VALUE
        arr[j + 1] = value

    return None