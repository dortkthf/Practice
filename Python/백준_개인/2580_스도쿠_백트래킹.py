import sys

input = sys.stdin.readline

row = []
col = [[] for i in range(9)]
box = [[[] for i in range(3)] for i in range(3)]
cnt = 0

for i in range(9):
    sudoku = list(map(int, input().split()))
    row.append(sudoku)
    boxrow = cnt // 3
    for j in range(9):
        col[j].append(sudoku[j])
        boxcol = j // 3
        box[boxrow][boxcol].append(sudoku[j])
    cnt += 1


def dfs():
    for i in range(9):
        for j in range(9):
            if row[i][j] == 0:
                boxrow = i // 3
                boxcol = j // 3
                for k in range(1, 10):
                    if k in row[i] or k in col[j] or k in box[boxrow][boxcol]:
                        continue
                    row[i][j] = k
                    col[j][i] = k
                    zero = box[boxrow][boxcol].index(0)
                    box[boxrow][boxcol][zero] = k
                    dfs()
                    row[i][j] = 0
                    col[j][i] = 0
                    zero = box[boxrow][boxcol].index(k)
                    box[boxrow][boxcol][zero] = 0
                if row[i][j] == 0:
                    return
            if i == 8 and j == 8 and row[i][j] != 0:
                break
        if i == 8 and j == 8 and row[i][j] != 0:
            print()
            for p in row:
                print(*p, sep=" ")
            exit(0)


dfs()
