def possible_state(temp):
    d = []
    ind = temp.index(-1)
    if ind not in [0, 1, 2]:
        d.append('u')
    if ind not in [6, 7, 8]:
        d.append('d')
    if ind not in [0, 3, 6]:
        d.append('l')
    if ind not in [2, 5, 8]:
        d.append('r')
    return d


def gen_state(state, d):
    temp = state.copy()
    ind = temp.index(-1)
    if 'u' in d:
        temp[ind], temp[ind-3] = temp[ind-3], temp[ind]
    if 'd' in d:
        temp[ind], temp[ind+3] = temp[ind+3], temp[ind]
    if 'l' in d:
        temp[ind], temp[ind-1] = temp[ind-1], temp[ind]
    if 'r' in d:
        temp[ind], temp[ind+1] = temp[ind+1], temp[ind]
    return temp


def solve(src, tar, vis, limit):
    if limit <= 0:
        return False
    display(src)
    if src == tar:
        print("Target State Achieved")
        return True
    vis.append(src)
    d = possible_state(src)
    for i in d:
        lst = gen_state(src, i)
        if lst not in vis:
            if solve(lst, tar, vis, limit-1):
                return True
    return False


def display(lst):
    x = 0
    for i in range(3):
        for j in range(3):
            print(lst[x], end='\t')
            x += 1
        print("\n")
    print("\n")


def main():
    src = []
    tar = []
    vis = []
    print("Enter source:")
    for i in range(9):
        src.append(int(input()))
    display(src)
    print("Enter target:")
    for i in range(9):
        tar.append(int(input()))
    display(tar)
    for i in range(1, 101):
        if (solve(src, tar, vis, i)):
            return


main()
