#include "../master.h"

// GENERATE RANDOM DATA
int *random_data(int size, int minimum, int maximum)
{
    // ALLOCATE ARRAY
    int *arr = malloc(size * sizeof(int));

    // FILL ARRAY
    for (int i = 0; i < size; i++)
        arr[i] = minimum + rand() % (maximum - minimum + 1);

    return arr;
}

// GENERATE SORTED DATA
int *sorted_data(int size, int minimum, int step)
{
    // ALLOCATE ARRAY
    int *arr = malloc(size * sizeof(int));

    // FILL ARRAY
    for (int i = 0; i < size; i++)
        arr[i] = minimum + i * step;

    return arr;
}

// GENERATE REVERSE DATA
int *reverse_sorted_data(int size, int minimum, int step)
{
    // CREATE SORTED ARRAY
    int *arr = sorted_data(size, minimum, step);

    // REVERSE ARRAY
    for (int i = 0; i < size / 2; i++)
    {
        int temp = arr[i];
        arr[i] = arr[size - 1 - i];
        arr[size - 1 - i] = temp;
    }

    return arr;
}

// GENERATE PARTIAL DATA
int *partially_sorted_data(
    int size,
    int minimum,
    int maximum,
    double sorted_percent
)
{
    // CREATE RANDOM ARRAY
    int *arr = random_data(size, minimum, maximum);

    // CALCULATE SORTED SIZE
    int sorted_size = (int)(size * sorted_percent);

    // SORT FIRST PART
    for (int i = 1; i < sorted_size; i++)
    {
        int value = arr[i];
        int j = i - 1;

        while (j >= 0 && arr[j] > value)
        {
            arr[j + 1] = arr[j];
            j--;
        }

        arr[j + 1] = value;
    }

    return arr;
}
