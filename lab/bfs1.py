def possible_states(temp):
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


def gen_states(temp1, ch):
    temp = temp1.copy()
    ind = temp.index(-1)
    if ch == 'd':
        temp[ind], temp[ind+3] = temp[ind+3], temp[ind]
    if ch == 'u':
        temp[ind], temp[ind-3] = temp[ind-3], temp[ind]
    if ch == 'l':
        temp[ind], temp[ind-1] = temp[ind-1], temp[ind]
    if ch == 'r':
        temp[ind], temp[ind+1] = temp[ind+1], temp[ind]
    return temp


def display(source):
    x = 0
    for i in range(3):
        for j in range(3):
            print(source[x], end=" ")
            x = x+1
        print("\n")


def solve(src, tar):
    if (src == tar):
        print("target achieved")
        return
    q = []
    vis = []
    q.append(src)
    print("Possible Moves:")
    while len(q) > 0:
        temp = q.pop(0)
        print()
        display(temp)
        if (temp == tar):
            print("target achieved")
            return
        vis.append(temp)
        d = possible_states(temp)
        for i in d:
            temp1 = gen_states(temp, i)
            if temp1 not in vis and temp1 not in q:
                q.append(temp1)


def main():
    print("Enter src list")
    src = []
    for i in range(9):
        src.append(int(input()))
    print("Source :")
    display(src)
    print("Enter target list")
    tar = []
    for i in range(9):
        tar.append(int(input()))
    print("Target :")
    display(tar)
    solve(src, tar)


main()
