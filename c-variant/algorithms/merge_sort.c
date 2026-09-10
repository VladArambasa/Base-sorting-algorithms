// MERGE SORT - IMPL

#include "../master.h"

// MERGE TWO HALVES
void merge(int arr[], int first, int mid, int last)
{
    // CALCULATE SIZES
    int left_size = mid - first + 1;
    int right_size = last - mid;

    // ALLOCATE TEMP ARRAYS
    int *left = malloc(left_size * sizeof(int));
    int *right = malloc(right_size * sizeof(int));

    // COPY LEFT HALF
    for (int i = 0; i < left_size; i++)
        left[i] = arr[first + i];

    // COPY RIGHT HALF
    for (int i = 0; i < right_size; i++)
        right[i] = arr[mid + 1 + i];

    // SET POINTERS
    int i = 0;
    int j = 0;
    int k = first;

    // MERGE VALUES
    while (i < left_size && j < right_size)
    {
        if (left[i] <= right[j])
        {
            arr[k] = left[i];
            i++;
        }
        else
        {
            arr[k] = right[j];
            j++;
        }

        k++;
    }

    // COPY LEFT REMAINDER
    while (i < left_size)
    {
        arr[k] = left[i];
        i++;
        k++;
    }

    // COPY RIGHT REMAINDER
    while (j < right_size)
    {
        arr[k] = right[j];
        j++;
        k++;
    }

    // FREE TEMP ARRAYS
    free(left);
    free(right);
}

// SORT USING MERGE SORT
void merge_sort(int arr[], int first, int last)
{
    // STOP AT ONE ELEMENT
    if (first >= last)
        return;

    // FIND MIDDLE
    int mid = (first + last) / 2;

    // SORT LEFT HALF
    merge_sort(arr, first, mid);

    // SORT RIGHT HALF
    merge_sort(arr, mid + 1, last);

    // MERGE HALVES
    merge(arr, first, mid, last);
}
