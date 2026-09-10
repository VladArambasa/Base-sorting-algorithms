#ifndef DATA_GENERATOR_H
#define DATA_GENERATOR_H

int *random_data(int size, int minimum, int maximum);
int *sorted_data(int size, int minimum, int step);
int *reverse_sorted_data(int size, int minimum, int step);
int *partially_sorted_data(
    int size,
    int minimum,
    int maximum,
    double sorted_percent
);

#endif
