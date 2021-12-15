import random as r
ai, player = 'O', 'X'
weights = [[3, 2, 3], [2, 4, 2], [3, 2, 3]]
board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]


def init():
    global board, weights, ai, player
    ai, player = 'O', 'X'
    weights = [[3, 2, 3], [2, 4, 2], [3, 2, 3]]
    board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]


def compare_line(lst, ch):
    return '-' in lst and lst.count(ch) == 2


def move(row, col, ch):
    global board, weights
    if board[row][col] == '-':
        board[row][col] = ch
        weights[row][col] = 0
        return True
    return False


def attacking_position(ch):
    global board, weights, ai, player
    for i in range(0, 3):
        col = [board[0][i], board[1][i], board[2][i]]
        if compare_line(col, ch):
            return (board[i].index('-'), i)
        elif compare_line(board[i], ch):
            return (i, board[i].index('-'))
    diag1 = [board[0][0], board[1][1], board[2][2]]
    diag2 = [board[0][2], board[1][1], board[2][0]]
    if compare_line(diag1, ch):
        return (diag1.index('-'), diag1.index('-'))
    if compare_line(diag2, ch):
        return (diag2.index('-'), 2-diag2.index('-'))
    return False


def display(move_type='board'):
    if move_type == 'cpu':
        print('*'*5+'CPU MOVE'+'*'*5)
    elif move_type == 'board':
        print("*"*5+'  Board of Tic Tac Toe '+'*'*5)
    else:
        print('*'*5+'PLAYER MOVE'+'*'*5)
    for i in range(3):
        for j in range(3):
            print(board[i][j], end='\t')
        print('\n')
    print('\n')


def get_position():
    max_value = max([max(x) for x in weights])
    positions = [(i, weights[i].index(max_value))
                 for i in range(3) if max_value in weights[i]]
    return positions


def has_tied():
    global board
    for i in range(0, 3):
        if '-' in board[i]:
            return False
    return True


def ai_move():
    global ai, player
    pos, f = attacking_position(ch=ai), False
    if pos != False:
        (row, col), f = pos, True
    else:
        pos = attacking_position(ch=player)
        if pos != False:
            row, col = pos
        else:
            row, col = r.choice(get_position())
    move(row, col, ai)
    return f


def run():
    global ai, player
    end, tied, move_type = False, False, None
    print('*'*10 + 'Tic Tac Toe'+'*'*10+'\n')
    display()
    ch = input('Choose a Character X or O : ')
    if ch == 'O':
        ai, player = player, ai
    while(True):
        if tied:
            print('*'*10+'The match is tied'+'*'*10)
            return
        elif end:
            print('*'*10+move_type+' has own '+'*'*10)
            return
        move_type = 'player'
        r = int(input("\nEnter next move's row (1 to 3): "))
        c = int(input("Enter next move's column (1 to 3): "))
        if not move(r-1, c-1, player):
            print('\nEnter proper positions!!')
        else:
            display(move_type=move_type)
            tied = has_tied()
            if tied:
                continue
            move_type = 'cpu'
            end = ai_move()
            display(move_type=move_type)
            tied = has_tied()


def main():
    run()
    f = 'Y'
    while(f == 'Y' or f == 'y'):
        f = input('Do you want to play again Y or N: ')
        init()
        if f == 'Y' or f == 'y':
            run()
    print('\n\n'+'*'*10+' Thank You '+'*'*10)


main()
