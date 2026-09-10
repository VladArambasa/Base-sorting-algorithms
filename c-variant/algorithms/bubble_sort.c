// BUBBLE SORT - IMPL

#include "../master.h"

// SORT USING BUBBLE SORT
void bubble_sort(int arr[], int size)
{
    // REPEAT PASSES
    for (int i = size - 1; i > 0; i--)
    {
        // TRACK SWAPS
        int swapped = 0;

        // COMPARE NEIGHBOURS
        for (int j = 0; j < i; j++)
        {
            // SWAP IF NEEDED
            if (arr[j] > arr[j + 1])
            {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;

                swapped = 1;
            }
        }

        // STOP IF SORTED
        if (!swapped)
            break;
    }
}
