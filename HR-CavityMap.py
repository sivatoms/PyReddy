# You are given a square map as a matrix of integer strings. Each cell of the map has a value denoting its depth. We will call a cell of the map a cavity if and only if this cell is not on the border of the map and each cell adjacent to it has strictly smaller depth. Two cells are adjacent if they have a common side, or edge.
#
# Find all the cavities on the map and replace their depths with the uppercase character X.

## MATRIX GRID PROBLEM
# CHECKING THE LEFT, RIGHT, BOTTOM, TOP VALUES EITHER GREATER OR LESS THAN THE CENTER VALUE OF A GRID

n = int(input())
grid = []
for i in range(n):
    k = list(input().strip())
    grid.append(k)

for i in range(1, (n - 2) + 1):
    for j in range(1, (n - 2) + 1):
        if grid[i][j] > max(grid[i - 1][j], grid[i + 1][j], grid[i][j - 1], grid[i][j + 1]):
            grid[i][j] = 'X'

for i in range(n):
    print(''.join(grid[i]))

# input
# 4
# 1112
# 1912
# 1892
# 1234

# output
# 1112
# 1X12
# 18X2
# 1234