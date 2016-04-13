#Game of Life

##Goal
Cells to experience the life cycle


###World
*two-dimensional orthogonal grid of square cells, 
    *each of which is in one of two possible states, alive or dead. 



###Cells
    Every cell interacts with its eight neighbors, which are the cells that are
     horizontally, vertically, or diagonally adjacent. At each step in time, the 
     following transitions occur
        *Any live cell with fewer than two live neighbors dies, as if caused by 
    under-population.
        *Any live cell with two or three live neighbors lives on to the next 
    generation.
        *Any live cell with more than three live neighbors dies, as if by 
    overcrowding.
        *Any dead cell with exactly three live neighbors becomes a live cell, as if 
    by reproduction.