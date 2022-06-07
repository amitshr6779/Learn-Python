#print 2D list
number_grid = [
    [1,2], [3,4], [5,6], [7,8], [9,10]
]

print(number_grid)

#print one items form 2d list
number_grid = [
    [1,2],
    [3,4], 
    [5,6], 
    [7,8], 
    [9,10]
]

print(number_grid[0])

#print specfic value from whole list
number_grid = [
    [1,2],
    [3,4], 
    [5,6], 
    [7,8], 
    [9,10]
]

print(number_grid[0][0])
print(number_grid[2][0])

#Use of nested for_lop:
number_grid = [
    [1,2,7],
    [3,4,6],
    [5,6,8], 
    [7,8,9], 
    [9,10,5]
]

for row in number_grid:
    for col in row:
        print(col)