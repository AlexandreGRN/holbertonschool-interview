#!/usr/bin/python3
# Check the surrounding cells of a cell
def checkSurrounding(grid, row, cell):
    perimeter = 4
    if row != 0 and grid[row - 1][cell] == 1:
        perimeter -= 1
    if row != len(grid) - 1 and grid[row + 1][cell] == 1:
        perimeter -= 1
    if cell != 0 and grid[row][cell - 1] == 1:
        perimeter -= 1
    if cell != len(grid[row]) - 1 and grid[row][cell + 1] == 1:
        perimeter -= 1
    return perimeter

# Island
def island_perimeter(grid):
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += checkSurrounding(grid, i, j)
    return perimeter
