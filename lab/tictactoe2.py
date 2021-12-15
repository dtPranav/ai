import random as r
board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
weights = [[3, 2, 3], [2, 4, 2], [3, 2, 3]]
ai, player = 'X', 'O'


def init():
    global board, weights, ai, player
    board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    weights = [[3, 2, 3], [2, 4, 2], [3, 2, 3]]
    ai, player = 'X', 'O'


def compare_line(lst, ch):
    return '_' in lst and lst.count(ch) == 2


def get_position():
    max_value = max([max(x) for x in weights])
    positions = [(i, weights[i].index(max_value))
                 for i in range(3) if max_value in weights[i]]
    return positions

# def get_position():
#     global board, weights, ai, player
#     m = max([max(i) for i in board])
#     return [(i, i.index(m)) for i in range(3) if m in board[i]]


def move(row, col, ch):
    global board, weights, ai, player
    if board[row][col] == '_':
        board[row][col], weights[row][col] = ch, 0
        return True
    return False


def attacking_position(ch):
    global board, weights, ai, player
    for i in range(0, 3):
        col = [board[0][i], board[1][i], board[2][i]]
        if compare_line(col, ch):
            return col.index('_'), i
        elif compare_line(board[i], ch):
            return i, board[i].index('_')
    diag1, diag2 = [board[0][0], board[1][1], board[2][2]], [
        board[0][2], board[1][1], board[2][0]]
    if compare_line(diag1, ch):
        return diag1.index('_'), diag1.index('_')
    if compare_line(diag2, ch):
        return diag2.index('_'), 2-diag2.index('_')
    return False


def ai_move():
    global board, weights, ai, player
    f = False
    pos = attacking_position(ai)
    if pos != False:
        (row, col), f = pos, True
    else:
        pos = attacking_position(player)
        if pos != False:
            row, col = pos
        else:
            row, col = r.choice(get_position())
    move(row, col, ai)
    return f


def has_tied():
    for i in board:
        if '_' in i:
            return False
    return True


def display(ch='board'):
    global player, ai
    if ch == player:
        print('*'*5+"Player's move"+'*'*5)
    elif ch == ai:
        print('*'*5+"CPU's move"+'*'*5)
    else:
        print('*'*5+"Board"+'*'*5)
    # for i in board:
    #     for j in i:
    #         print(j, endl='\t')
    #     print("\n")
    for i in range(3):
        for j in range(3):
            print(board[i][j], end='\t')
        print('\n')
    print('\n')


def run():
    global ai, player, board, weights
    m = player
    tied = False
    end = False
    display()
    while(True):
        if tied:
            print("The match has tied")
            return
        if end:
            print("Cpu has won")
            return
        if (m == player):
            row = int(input("Enter row (1-3): "))
            col = int(input("Enter col (1-3): "))
            if move(row-1, col-1, m):
                display(m)
                m = ai
        else:
            tied = has_tied()
            if tied:
                print("The match has tied")
                return
            else:
                end = ai_move()
                display(m)
                tied = has_tied()
                m = player


def main():
    flag = 'y'
    while(flag == 'y'):
        init()
        run()
        flag = input("Do you wish to continue (y/n)")
    print("Thanks for playing")


main()
