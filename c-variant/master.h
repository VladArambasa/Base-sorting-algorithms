#ifndef MASTER_H
#define MASTER_H

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "algorithms/bubble_sort.h"
#include "algorithms/quick_sort.h"
#include "algorithms/merge_sort.h"
#include "algorithms/insertion_sort.h"
#include "algorithms/selection_sort.h"

#include "src/data_generator.h"
#include "src/helpers.h"

#define TIMELIM_SMALL 30
#define TIMELIM_LARGE 180

#define DATA_RANDOM 1
#define DATA_SORTED 2
#define DATA_REVERSE 3
#define DATA_PARTIAL 4

#endif
