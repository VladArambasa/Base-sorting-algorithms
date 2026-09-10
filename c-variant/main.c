#include "master.h"

// TEST BUBBLE SORT
void test_bubble_sort(int original[], int size)
{
    int *arr = malloc(size * sizeof(int));

    for (int i = 0; i < size; i++)
        arr[i] = original[i];

    clock_t start = clock();

    bubble_sort(arr, size);

    clock_t end = clock();

    printf("Bubble Sort: %.6f seconds - %s\n",
           get_time(start, end),
           check_sorted(arr, size) ? "OK" : "FAILED");

    free(arr);
}

// TEST QUICK SORT
void test_quick_sort(int original[], int size)
{
    int *arr = malloc(size * sizeof(int));

    for (int i = 0; i < size; i++)
        arr[i] = original[i];

    clock_t start = clock();

    quick_sort(arr, 0, size - 1);

    clock_t end = clock();

    printf("Quick Sort: %.6f seconds - %s\n",
           get_time(start, end),
           check_sorted(arr, size) ? "OK" : "FAILED");

    free(arr);
}

// TEST MERGE SORT
void test_merge_sort(int original[], int size)
{
    int *arr = malloc(size * sizeof(int));

    for (int i = 0; i < size; i++)
        arr[i] = original[i];

    clock_t start = clock();

    merge_sort(arr, 0, size - 1);

    clock_t end = clock();

    printf("Merge Sort: %.6f seconds - %s\n",
           get_time(start, end),
           check_sorted(arr, size) ? "OK" : "FAILED");

    free(arr);
}

// TEST INSERTION SORT
void test_insertion_sort(int original[], int size)
{
    int *arr = malloc(size * sizeof(int));

    for (int i = 0; i < size; i++)
        arr[i] = original[i];

    clock_t start = clock();

    insertion_sort(arr, size);

    clock_t end = clock();

    printf("Insertion Sort: %.6f seconds - %s\n",
           get_time(start, end),
           check_sorted(arr, size) ? "OK" : "FAILED");

    free(arr);
}

// TEST SELECTION SORT
void test_selection_sort(int original[], int size)
{
    int *arr = malloc(size * sizeof(int));

    for (int i = 0; i < size; i++)
        arr[i] = original[i];

    clock_t start = clock();

    selection_sort(arr, size);

    clock_t end = clock();

    printf("Selection Sort: %.6f seconds - %s\n",
           get_time(start, end),
           check_sorted(arr, size) ? "OK" : "FAILED");

    free(arr);
}

int main(void)
{
    // INITIALISE RANDOM GENERATOR
    srand((unsigned int)time(NULL));

    // SET ARRAY SIZE
    int size = 10000;

    // GENERATE DATA
    int *data = random_data(size, 0, 100000);

    printf("Array size: %d\n\n", size);

    // RUN ALGORITHMS
    test_bubble_sort(data, size);
    test_quick_sort(data, size);
    test_merge_sort(data, size);
    test_insertion_sort(data, size);
    test_selection_sort(data, size);

    // FREE ORIGINAL DATA
    free(data);

    return 0;
}
