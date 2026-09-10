import time

# SORT USING SELECTION SORT
def selection_sort(arr, time_limit, start_time):
    # LOOP THROUGH ARRAY
    for i in range(len(arr) - 1):
        # CHECK TIME
        if time.time() - start_time >= time_limit:
            return "DNF"

        # ASSUME CURRENT VALUE IS MINIMUM
        min_index = i

        # FIND MINIMUM
        for j in range(i + 1, len(arr)):
            # CHECK TIME
            if time.time() - start_time >= time_limit:
                return "DNF"

            if arr[j] < arr[min_index]:
                min_index = j

        # SWAP MINIMUM INTO PLACE
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return None