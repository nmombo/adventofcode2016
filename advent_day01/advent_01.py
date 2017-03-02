#############################################################
# IMPORT NUMPY
import numpy as np
import matplotlib.pyplot as plt
plt.show(block=False)

#############################################################
# INPUT DATA
instructions = 'R2, L3, R4, L5, R6, R7, L8, L9, R10, R11'   # test case for part A
instructions = 'R8, R4, R4, R8'                             # test case for part B
instructions = 'L1, R3, R1, L5, L2, L5, R4, L2, R2, R2, L2, R1, L5, R3, L4, L1, L2, R3, R5, L2, R5, L1, R2, L5, R4, R2, R2, L1, L1, R1, L3, L1, R1, L3, R5, R3, R3, L4, R4, L2, L4, R1, R1, L193, R2, L1, R54, R1, L1, R71, L4, R3, R191, R3, R2, L4, R3, R2, L2, L4, L5, R4, R1, L2, L2, L3, L2, L1, R4, R1, R5, R3, L5, R3, R4, L2, R3, L1, L3, L3, L5, L1, L3, L3, L1, R3, L3, L2, R1, L3, L1, R5, R4, R3, R2, R3, L1, L2, R4, L3, R1, L1, L1, R5, R2, R4, R5, L1, L1, R1, L2, L4, R3, L1, L3, R5, R4, R3, R3, L2, R2, L1, R4, R2, L3, L4, L2, R2, R2, L4, R3, R5, L2, R2, R4, R5, L2, L3, L2, R5, L4, L2, R3, L5, R2, L1, R1, R3, R3, L5, L2, L2, R5'    
                                                            # case for submission
        
#############################################################
# PARSE DATA

# find the number of commas
num_commas = 1
dir_temp = instructions
while( dir_temp.find(',') > -1):
    dir_temp = dir_temp[dir_temp.find(',')+1:]
    num_commas = num_commas + 1
        
# take all the directions
dir_temp = instructions
directions = ''
i = 1
while i < num_commas:
    directions = directions + dir_temp[0]
    dir_temp = dir_temp[dir_temp.find(' ') + 1:]
    i = i + 1
directions = directions + dir_temp[0]
    
# take all the numbers
dir_temp = instructions[1:]
numbers = np.zeros(len(directions))
i = 0
while i < num_commas-1:
    index_comma = dir_temp.find(',')
    numbers[i] = int(dir_temp[0:index_comma])
    dir_temp = dir_temp[index_comma+3:]
    i = i + 1
numbers[i] = int(dir_temp)

#############################################################
# CALCULATE MOVEMENT

x, y = 0, 0
cur_dir = 0    # north is 0, east is 1, south is 2, west is 3
xlog, ylog = [0], [0]
i = 0
while i < len(directions):
    # change direction
    if directions[i] == 'R':
        cur_dir = cur_dir + 1
    else:
        cur_dir = cur_dir - 1
    # correct out-of-bounds directions
    if cur_dir < 0:
        cur_dir = cur_dir + 4
    if cur_dir > 3:
        cur_dir = cur_dir - 4
    # move in the new direction
    if cur_dir == 0:
        j = 0
        while j < numbers[i]:
            y += 1
            j += 1
            xlog.extend([x])
            ylog.extend([y])
    if cur_dir == 1:
        j = 0
        while j < numbers[i]:
            x += 1
            j += 1
            xlog.extend([x])
            ylog.extend([y])
    if cur_dir == 2:
        j = 0
        while j < numbers[i]:
            y -= 1
            j += 1
            xlog.extend([x])
            ylog.extend([y])
    if cur_dir == 3:
        j = 0
        while j < numbers[i]:
            x -= 1
            j += 1
            xlog.extend([x])
            ylog.extend([y])
    # iterate
    i += 1
    
distance = abs(x) + abs(y)
print 'distance                 ' + str(distance)

#############################################################
# CALCULATE FIRST INTERSECTION

i = 1
found = False
while i < np.size(xlog):
    j = 0
    while j < i:
        if xlog[i] == xlog[j] and ylog[i] == ylog[j]:
            found = True
            break
        j += 1
    if found:
        break
    i += 1
distance_intersect = abs(xlog[j]) + abs(ylog[j])
print 'distance first intersect: ' + str(distance_intersect)

plt.figure(1)
plt.plot(xlog, ylog)
plt.show()