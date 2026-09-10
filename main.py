import csv

# IMPORT ALL PROJECT FUNCTION
from master import *

# TIME LIMITS
TIMELIM_SMALL = 30
TIMELIM_LARGE = 180


# GET TIME LIMIT
def get_time_limit(size):
    # USE LONGER LIMIT FOR LARGE DATA
    if size > 10000:
        return TIMELIM_LARGE

    return TIMELIM_SMALL


# RUN ALL ALGORITHMS
def run_all_algorithms(data):
    # GET ARRAY SIZE
    size = len(data)

    # GET TIME LIMIT
    time_limit = get_time_limit(size)

    # STORE RESULTS
    results = []

    # RUN QUICKSORT
    results.append(
        run_quicksort(
            quicksort,
            data,
            time_limit
        )
    )

    # RUN MERGE SORT
    results.append(
        run_algorithm(
            merge_sort_wrapper,
            data,
            time_limit
        )
    )

    # RUN BUBBLE SORT
    results.append(
        run_algorithm(
            bubble_sort,
            data,
            time_limit
        )
    )

    # RUN INSERTION SORT
    results.append(
        run_algorithm(
            insertion_sort,
            data,
            time_limit
        )
    )

    # RUN SELECTION SORT
    results.append(
        run_algorithm(
            selection_sort,
            data,
            time_limit
        )
    )

    return results


# WRAP MERGE SORT
def merge_sort_wrapper(arr, time_limit, start_time):
    # RUN MERGE SORT
    return merge_sort(
        arr,
        0,
        len(arr) - 1,
        time_limit,
        start_time
    )


# DEFINE TESTS
tests = [
    {
        "name": "random_10",
        "size": 10,
        "type": "random",
        "minimum": 1,
        "maximum": 100
    },
    {
        "name": "random_500",
        "size": 500,
        "type": "random",
        "minimum": 1,
        "maximum": 200
    },
    {
        "name": "random_10000",
        "size": 10000,
        "type": "random",
        "minimum": 1,
        "maximum": 3000
    },
    {
        "name": "random_1000000",
        "size": 1000000,
        "type": "random",
        "minimum": 1,
        "maximum": 2000000
    },
    {
        "name": "sorted_10",
        "size": 10,
        "type": "sorted"
    },
    {
        "name": "sorted_500",
        "size": 500,
        "type": "sorted"
    },
    {
        "name": "sorted_10000",
        "size": 10000,
        "type": "sorted"
    },
    {
        "name": "sorted_1000000",
        "size": 1000000,
        "type": "sorted"
    },
    {
        "name": "reverse_10",
        "size": 10,
        "type": "reverse"
    },
    {
        "name": "reverse_500",
        "size": 500,
        "type": "reverse"
    },
    {
        "name": "reverse_10000",
        "size": 10000,
        "type": "reverse"
    },
    {
        "name": "partial_10000",
        "size": 10000,
        "type": "partial",
        "minimum": 1,
        "maximum": 3000,
        "sorted_percent": 0.5
    }
]


# OPEN RESULTS FILE
with open("Data.csv", "w", newline="") as csvfile:
    # CREATE CSV WRITER
    csvwriter = csv.writer(csvfile)

    # WRITE HEADER
    csvwriter.writerow(
        [
            "Test",
            "Quick Sort",
            "Merge Sort",
            "Bubble Sort",
            "Insertion Sort",
            "Selection Sort"
        ]
    )

    # RUN EACH TEST
    for test in tests:
        # GENERATE DATA
        data = generate_data(
            size=test["size"],
            data_type=test["type"],
            minimum=test.get("minimum", 1),
            maximum=test.get("maximum", 100),
            sorted_percent=test.get("sorted_percent", 0.5)
        )

        # RUN ALGORITHMS
        results = run_all_algorithms(data)

        # WRITE RESULTS
        csvwriter.writerow(
            [
                test["name"],
                *results
            ]
        )

        # SHOW PROGRESS
        print(test["name"], results)