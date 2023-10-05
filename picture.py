grid = [
 ['.', '.', '.', '.', '.', '.'],
 ['.', 'O', 'O', '.', '.', '.'],
 ['O', 'O', 'O', 'O', '.', '.'],
 ['O', 'O', 'O', 'O', 'O', '.'],
 ['.', 'O', 'O', 'O', 'O', 'O'],
 ['O', 'O', 'O', 'O', 'O', '.'],
 ['O', 'O', 'O', 'O', '.', '.'],
 ['.', 'O', 'O', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.'] ]


#this is for the x coodinate--because there are 6 elements in a list
for x in range(6):
#this is for the y coodinate--because there are 9 list
    for y in range(9):
        if y!= 8:
            print(grid[y][x], end = "")
        else:
            print(grid[8][x])