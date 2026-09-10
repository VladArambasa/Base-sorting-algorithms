import time

# CHECK IF ARRAY IS SORTED
def check_sorted(arr):
    # CHECK EACH PAIR
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False

    return True


# RUN ONE ALGORITHM
def run_algorithm(algorithm, data, time_limit):
    # COPY INPUT DATA
    test = data.copy()

    # START TIMER
    start_time = time.time()

    # RUN ALGORITHM
    result = algorithm(
        test,
        time_limit,
        start_time
    )

    # CALCULATE TIME
    elapsed_time = time.time() - start_time

    # CHECK DNF
    if result in ["DNF", "DNF-rec limit"]:
        return "DNF"

    # CHECK SORTING
    if not check_sorted(test):
        return f"Not sorted correctly, time:{elapsed_time}"

    return elapsed_time


# RUN QUICKSORT
def run_quicksort(algorithm, data, time_limit):
    # COPY INPUT DATA
    test = data.copy()

    # START TIMER
    start_time = time.time()

    # RUN QUICKSORT
    result = algorithm(
        test,
        0,
        len(test) - 1,
        time_limit,
        start_time,
        0
    )

    # CALCULATE TIME
    elapsed_time = time.time() - start_time

    # CHECK DNF
    if result in ["DNF", "DNF-rec limit"]:
        return "DNF"

    # CHECK SORTING
    if not check_sorted(test):
        return f"Not sorted correctly, time:{elapsed_time}"

    return elapsed_time