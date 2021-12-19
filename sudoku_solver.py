import numpy as np

grid = [[0,3,5,0,0,0,1,0,0],
        [2,0,9,0,0,6,0,0,0],
        [0,0,0,0,0,9,2,0,0],
        [6,0,0,3,9,0,0,0,0],
        [0,7,4,0,0,0,8,1,0],
        [0,0,0,0,4,7,0,0,5],
        [0,0,6,7,0,0,0,0,0],
        [0,0,0,9,0,0,4,0,7],
        [0,0,1,0,0,0,5,8,0]]

np_grid = np.array(grid)


def possible(number, coordinate):
    row, col = coordinate

    lbound_row, lbound_col = row//3 * 3, col//3 * 3
    ubound_row, ubound_col = lbound_row + 3, lbound_col + 3

    same_box = number in np_grid[lbound_row:ubound_row, lbound_col:ubound_col]
    same_row = number in np_grid[row]
    same_column = number in np_grid[:, col]
    
    if any((same_row, same_column, same_box)):
        return False
    return True


def solve(grid):
    for idx, elem in np.ndenumerate(grid):
        if elem != 0:
            continue
        for n in range(1, 10):
            if possible(n, idx):
                grid[idx] = n
                solve(grid)
                grid[idx] = 0
        return
    print(grid)


if __name__ == '__main__':
    solve(np_grid)
