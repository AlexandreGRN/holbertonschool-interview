#include "slide_line.h"
#include <stdio.h>

size_t move_left(int *line, size_t size, size_t index, size_t stop_at)
{
    (void) size;
    for (size_t i = index ; i > 0; i--)
    {
        // Move left if preceding is 0
        if (line[i - 1] == 0)
        {
            line[i - 1] = line[i];
            line[i] = 0;
        }
        // Fuze together if preceding is equal
        if (line[i] == line[i - 1] && stop_at < i)
        {
            line[i - 1] *= 2;
            line[i] = 0;
            return (i);
        }
    }
    return (stop_at);
}

size_t move_right(int *line, size_t size, size_t index, size_t stop_at)
{
    for (size_t i = index ; i < size - 1; i++)
    {
        // Move right if following is 0
        if (line[i + 1] == 0)
        {
            line[i + 1] = line[i];
            line[i] = 0;
        }
        // Fuze together if following is equal
        if (line[i] == line[i + 1] && i <= stop_at)
        {
            line[i + 1] *= 2;
            line[i] = 0;
            return (i);
        }
    }
    return (stop_at);
}

int slide_line(int *line, size_t size, int direction)
{
    size_t stop_at;
    if (direction == 0)
    {
        stop_at = 0;
        for (size_t i = 1; i < size; i++)
        {
            if (line[i] != 0)
            {
                stop_at = move_left(line, size, i, stop_at);
            }
        }
    } else {
        stop_at = size - 1;
        for (size_t i = size - 1; i + 1 > 0; i--)
        {
            if (line[i] != 0)
            {
                stop_at = move_right(line, size, i, stop_at);
            }
        }
    }
    return (1);
}

