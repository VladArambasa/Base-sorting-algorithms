// INSERTION SORT - IMPL

#include "../master.h"

// SORT USING INSERTION SORT
void insertion_sort(int arr[], int size)
{
    // LOOP THROUGH ARRAY
    for (int i = 1; i < size; i++)
    {
        // SAVE CURRENT VALUE
        int value = arr[i];

        // START FROM PREVIOUS VALUE
        int j = i - 1;

        // MOVE LARGER VALUES
        while (j >= 0 && arr[j] > value)
        {
            arr[j + 1] = arr[j];
            j--;
        }

        // INSERT VALUE
        arr[j + 1] = value;
    }
}
