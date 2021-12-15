import random as r


def clean(floor, row, col):
    i, j, p, q = row, col, len(floor), len(floor[0])
    Right = Down = True
    cleaned = [not any(fl)for fl in floor]
    print(cleaned)
    while not all(cleaned):
        while any(floor[i]):
            print_floor(floor, i, j)
            if floor[i][j]:
                floor[i][j] = 0
                print_floor(floor, i, j)
            if not any(floor[i]):
                cleaned[i] = True
                break
            if j == q-1:
                j -= 1
                Right = False
            elif j == 0:
                j += 1
                Right = True
            else:
                j += 1 if Right else -1
        if all(cleaned):
            break
        if i == p-1:
            i -= 1
            Down = False
        elif i == 0:
            i += 1
            Down = True
        else:
            i += 1 if Down else -1
        if cleaned[i]:
            print_floor(floor, i, j)


def print_floor(floor, row, col):
    for m in range(len(floor)):
        for n in range(len(floor[m])):
            if m == row and n == col:
                print(f">{floor[m][n]}<", end=' ')
            else:
                print(f"{floor[m][n]}", end='  ')
        print(end='\n')
    print(end='\n')


floor = [[1, 0, 0, 0],
         [0, 1, 0, 1],
         [1, 0, 1, 1]]
# int r=
clean(floor, 1, 2)
