#include "../master.h"

// CHECK IF ARRAY IS SORTED
int check_sorted(int arr[], int size)
{
    // CHECK EACH PAIR
    for (int i = 0; i < size - 1; i++)
    {
        if (arr[i] > arr[i + 1])
            return 0;
    }

    return 1;
}

// CALCULATE TIME
double get_time(clock_t start, clock_t end)
{
    // CONVERT TO SECONDS
    return (double)(end - start) / CLOCKS_PER_SEC;
}
