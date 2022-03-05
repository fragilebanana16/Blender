# Draw names with object in grid format
import bpy
import numpy as np
# red green yellow
grid = np.zeros((6,11), dtype=int)
# H part(0 for empty, 1 for H color, 2 for R color, 3 for T color)
for h in range(6):
    grid[h, 0] = 1
    grid[h, 2] = 1
grid[2, 1] = 1

# R part
for h in range(6):
    grid[h, 4] = 2
    grid[h, 5] = 2
    grid[h, 6] = 2
grid[1, 5] = 0
grid[3, 6] = 0
grid[4, 5] = 0
grid[5, 5] = 0

# T part
for h in range(6):
    grid[h, 9] = 3
grid[0, 8] = 3
grid[0, 10] = 3

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if (grid[i][j] > 0):
            bpy.ops.mesh.primitive_monkey_add(location=(i*3,j*3,0))
      #      print(x[i][j])