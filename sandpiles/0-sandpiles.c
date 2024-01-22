#include "sandpiles.h"

/**
* topple - topples the grid
* @grid: the grid to topple
* Return: void
*/
void topple(int grid[3][3])
{
	int grid_copy[3][3] = {
		{grid[0][0], grid[0][1], grid[0][2]},
		{grid[1][0], grid[1][1], grid[1][2]},
		{grid[2][0], grid[2][1], grid[2][2]}
	};

	for (int i = 0 ; i < 3 ; i++)
		for (int j = 0 ; j < 3 ; j++)
			if (grid_copy[i][j] > 3)
			{
				grid[i][j] -= 4;
				if (i - 1 >= 0)
					grid[i - 1][j] += 1;
				if (i + 1 <= 2)
					grid[i + 1][j] += 1;
				if (j - 1 >= 0)
					grid[i][j - 1] += 1;
				if (j + 1 <= 2)
					grid[i][j + 1] += 1;
			}
}

/**
 * print_grid_nl - Print 3x3 grid
 * @grid: 3x3 grid
 * Return: void
*/
void print_grid_nl(int grid[3][3])
{
	int i, j;

	printf("=\n");
	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			if (j)
				printf(" ");
			printf("%d", grid[i][j]);
		}
		printf("\n");
	}
}

/**
 * isStable - checks if the grid is stable
 * @grid: the grid to check
 * Return: 1 if stable, 0 if not
*/
int isStable(int grid[3][3])
{
	int stable = 1;

	for (int i = 0; i < 3; i++)
		for (int j = 0; j < 3; j++)
			if (grid[i][j] > 3)
				stable = 0;

	return (stable);
}

/**
 * sandpiles_sum - computes the sum of two sandpiles
 * @grid1: the first grid
 * @grid2: the second grid
 * Return: void
*/
void sandpiles_sum(int grid1[3][3], int grid2[3][3])
{
	/*Make new grid */
	int new_grid[3][3];

	/* Add grid1 and grid2 */
	for (int i = 0; i < 3; i++)
		for (int j = 0; j < 3; j++)
			new_grid[i][j] = grid1[i][j] + grid2[i][j];

	/* Topple new grid if needed and print it */
	while (isStable(new_grid) == 0)
	{
		print_grid_nl(new_grid);
		topple(new_grid);
	}

	/* Apply the changes to grid1 */
	for (int i = 0; i < 3; i++)
		for (int j = 0; j < 3; j++)
			grid1[i][j] = new_grid[i][j];
}