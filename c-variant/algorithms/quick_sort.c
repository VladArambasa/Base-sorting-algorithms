// QUICK SORT - IMPL

#include "../master.h"

// SORT USING QUICKSORT
void quick_sort(int arr[], int first, int last)
{
    // STOP AT ONE ELEMENT
    if (first >= last)
        return;

    // CHOOSE MIDDLE PIVOT
    int pivot = arr[(first + last) / 2];

    // SET POINTERS
    int i = first;
    int j = last;

    // PARTITION ARRAY
    while (i <= j)
    {
        // MOVE LEFT POINTER
        while (arr[i] < pivot)
            i++;

        // MOVE RIGHT POINTER
        while (arr[j] > pivot)
            j--;

        // SWAP VALUES
        if (i <= j)
        {
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;

            i++;
            j--;
        }
    }

    // SORT LEFT PART
    if (first < j)
        quick_sort(arr, first, j);

    // SORT RIGHT PART
    if (i < last)
        quick_sort(arr, i, last);
}
