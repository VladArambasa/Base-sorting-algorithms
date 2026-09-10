import time
import random

# GENERATE RANDOM DATA
def random_data(size, minimum, maximum):
    # CREATE RANDOM LIST
    return [
        random.randint(minimum, maximum)
        for _ in range(size)
    ]


# GENERATE SORTED DATA
def sorted_data(size, minimum=1, step=1):
    # CREATE SORTED LIST
    return [
        minimum + i * step
        for i in range(size)
    ]


# GENERATE REVERSE SORTED DATA
def reverse_sorted_data(size, minimum=1, step=1):
    # CREATE SORTED LIST
    data = sorted_data(size, minimum, step)

    # REVERSE LIST
    data.reverse()

    return data


# GENERATE PARTIALLY SORTED DATA
def partially_sorted_data(size, minimum, maximum, sorted_percent):
    # CREATE RANDOM LIST
    data = random_data(size, minimum, maximum)

    # FIND SORTED PART SIZE
    sorted_size = int(size * sorted_percent)

    # SORT PART OF LIST
    data[:sorted_size] = sorted(data[:sorted_size])

    return data


# GENERATE DUPLICATE DATA
def duplicate_data(size, minimum, maximum, number_of_values):
    # CREATE SMALL VALUE POOL
    values = random_data(
        number_of_values,
        minimum,
        maximum
    )

    # CHOOSE VALUES FROM POOL
    return [
        random.choice(values)
        for _ in range(size)
    ]


# GENERATE DATA BY TYPE
def generate_data(
    size,
    data_type,
    minimum=1,
    maximum=100,
    sorted_percent=0.5
):
    # CHOOSE RANDOM DATA
    if data_type == "random":
        return random_data(
            size,
            minimum,
            maximum
        )

    # CHOOSE SORTED DATA
    if data_type == "sorted":
        return sorted_data(
            size,
            minimum
        )

    # CHOOSE REVERSE DATA
    if data_type == "reverse":
        return reverse_sorted_data(
            size,
            minimum
        )

    # CHOOSE PARTIAL DATA
    if data_type == "partial":
        return partially_sorted_data(
            size,
            minimum,
            maximum,
            sorted_percent
        )

    # CHOOSE DUPLICATE DATA
    if data_type == "duplicates":
        return duplicate_data(
            size,
            minimum,
            maximum,
            10
        )

    # REJECT UNKNOWN TYPE
    raise ValueError("Unknown data type")