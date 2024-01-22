#ifndef SANDPILES_H
#define SANDPILES_H

#include <stdio.h>
void topple(int grid[3][3]);
void print_grid_nl(int grid[3][3]);
int isStable(int grid[3][3]);
void sandpiles_sum(int grid1[3][3], int grid2[3][3]);

#endif