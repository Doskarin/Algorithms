with open('day13.txt') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]
i = 0
coord = []

while lines[i] != "":
    coord.append(lines[i])
    i += 1
coord = [[int(c.split(",")[0]), int(c.split(",")[1])] for c in coord]
instructions = lines[i + 1:]
instructions = [line.split()[-1] for line in instructions]

rows = 0
cols = 0
for x, y in coord:
    rows = max(rows, y)
    cols = max(cols, x)
rows += 1
cols += 1
# print(rows, cols)
grid = [['.'] * cols for _ in range(rows)]
for x, y in coord:
    grid[y][x] = "#"

def fold(instruction, start, grid):
    R, C = len(grid), len(grid[0])
    if instruction == "x":
        for i in range(R):
            j = 1
            while start - j >= 0 and start + j < C:
                if grid[i][start - j] == "#":
                    j += 1
                    continue
                grid[i][start - j] = grid[i][start + j]
                j += 1
        return [row[:start] for row in grid]
    else:
        for j in range(C):
            i = 1
            while start - i >= 0 and start + i < R:
                if grid[start - i][j] == "#":
                    i += 1
                    continue
                grid[start - i][j] = grid[start + i][j]
                i += 1
        return grid[:start]


instructions = [[line.split("=")[0], int(line.split("=")[1])] for line in instructions]
for instruction, start in instructions:
    grid = fold(instruction, start, grid)
print(grid)



'''
[['#', '#', '#', '.', '.', '.', '#', '#', '.', '.', '#', '#', '#', '#', '.', '#', '#', '#', '.', '.', '.', '#', '#', '.', '.', '#', '#', '#', '#', '.', '.', '#', '#', '.', '.', '#', '#', '#', '.', '.'],
 ['#', '.', '.', '#', '.', '#', '.', '.', '#', '.', '.', '.', '.', '#', '.', '#', '.', '.', '#', '.', '#', '.', '.', '#', '.', '#', '.', '.', '.', '.', '#', '.', '.', '#', '.', '#', '.', '.', '#', '.'],
 ['#', '#', '#', '.', '.', '#', '.', '.', '.', '.', '.', '.', '#', '.', '.', '#', '.', '.', '#', '.', '#', '.', '.', '.', '.', '#', '#', '#', '.', '.', '#', '.', '.', '#', '.', '#', '#', '#', '.', '.'], 
 ['#', '.', '.', '#', '.', '#', '.', '.', '.', '.', '.', '#', '.', '.', '.', '#', '#', '#', '.', '.', '#', '.', '.', '.', '.', '#', '.', '.', '.', '.', '#', '#', '#', '#', '.', '#', '.', '.', '#', '.'], 
 ['#', '.', '.', '#', '.', '#', '.', '.', '#', '.', '#', '.', '.', '.', '.', '#', '.', '#', '.', '.', '#', '.', '.', '#', '.', '#', '.', '.', '.', '.', '#', '.', '.', '#', '.', '#', '.', '.', '#', '.'], 
 ['#', '#', '#', '.', '.', '.', '#', '#', '.', '.', '#', '#', '#', '#', '.', '#', '.', '.', '#', '.', '.', '#', '#', '.', '.', '#', '#', '#', '#', '.', '#', '.', '.', '#', '.', '#', '#', '#', '.', '.']]

'''