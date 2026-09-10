// SELECTION SORT - IMPL

#include "../master.h"

// SORT USING SELECTION SORT
void selection_sort(int arr[], int size)
{
    // LOOP THROUGH ARRAY
    for (int i = 0; i < size - 1; i++)
    {
        // ASSUME CURRENT VALUE IS MINIMUM
        int min_index = i;

        // FIND MINIMUM
        for (int j = i + 1; j < size; j++)
        {
            if (arr[j] < arr[min_index])
                min_index = j;
        }

        // SWAP VALUES
        int temp = arr[i];
        arr[i] = arr[min_index];
        arr[min_index] = temp;
    }
}
