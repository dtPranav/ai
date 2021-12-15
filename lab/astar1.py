def h(state, target):
    count = 0
    i = 0
    for i in range(0, 9):
        if state[i] != target[i]:
            count = count+1
    return count


def possible_states(src):
    d = []
    ind = src.index(-1)
    if ind not in [0, 3, 6]:
        d.append('l')
    if ind not in [0, 1, 2]:
        d.append('u')
    if ind not in [2, 5, 8]:
        d.append('r')
    if ind not in [6, 7, 8]:
        d.append('d')
    return d


def gen_state(temp, d):
    temp1 = temp.copy()
    i = temp1.index(-1)
    if d == 'u':
        temp1[i], temp1[i-3] = temp1[i-3], temp1[i]
    if d == 'l':
        temp1[i], temp1[i-1] = temp1[i-1], temp1[i]
    if d == 'r':
        temp1[i], temp1[i+1] = temp1[i+1], temp1[i]
    if d == 'd':
        temp1[i], temp1[i+3] = temp1[i+3], temp1[i]
    return temp1


def astar(src, tar):
    vis = []
    q = []
    q.append(src)
    g = 0
    while len(q):
        print(f'Level : {g}')
        moves = []
        for i in q:
            print(i)
            display(i)
            if i == tar:
                print("target achieved")
                return
            vis.append(i)
            d = possible_states(i)
            for j in d:
                move = gen_state(i, j)
                if move not in q and move not in vis:
                    moves.append(move)
        cost = [g + h(move, tar) for move in moves]
        q = [moves[i] for i in range(len(moves)) if cost[i] == min(cost)]
        g += 1


def display(src):
    temp = src.copy()
    temp[temp.index(-1)] = ' '
    print(f"""
{temp[0]}  {temp[1]}  {temp[2]}
{temp[3]}  {temp[4]}  {temp[5]}
{temp[6]}  {temp[7]}  {temp[8]}
    """)


def main():
    # src = []
    # print("Enter source :")
    # for i in range(9):
    #     src.append(int(input()))
    # display(src)
    # tar = []
    # print("Enter target :")
    # for i in range(9):
    #     tar.append(int(input()))
    # display(tar)
    src = [1, 2, 3, -1, 4, 5, 6, 7, 8]
    tar = [1, 2, 3, 4, 5, -1, 6, 7, 8]
    astar(src, tar)


main()
