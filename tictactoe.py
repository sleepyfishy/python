board = [['-','-','-'],['-','-','-'],['-','-','-']]
player1 = 'x'
player2 = 'o'


def check(input):
    if input in ['0','1','2']:
        return True
    else:
        return False


def print_board():
    for r in range(3):
        print(board[r][0],'|',board[r][1],'|',board[r][2])    


def move(turn):
    while True:
        while True:
            row = input('Please enter a row (0,1 or 2 [top to bottom]): ')
            check(row)
            if check(row) == True:
                row = int(row)
                break
            else:
                print('Invalid input.')
                continue

        while True:    
            col = input('Please enter a column (0,1 or 2 [right to left]): ')
            check(col)
            if check(col) == True:
                col = int(col)
                break
            else:
                print('Invalid input.')
                continue
        
        if (board[row][col] == 'x') or (board[row][col] == 'o'):
            print('Already occupied.')
            continue
        else:
            board[row][col] = turn
            break


def win(turn):
    for r in range(3):
        if (board[r][0] == board[r][1] == board[r][2] == turn) or (board[0][r] == board[1][r] == board[2][r] == turn):
            print('Player ', turn, ' has won.')
            return True
        
    if (board[0][0] == board[1][1] == board[2][2] == turn) or (board[0][2] == board[1][1] == board[2][0] == turn):
        print('Player ', turn, ' has won.')
        return True
    
    return False


def main():
    print('Starting game.')
    print_board()

    while True:
        turn = player1
        print('Player x to move.')
        move(turn)
        print_board()

        if win(turn) == True:
            break
        
        turn = player2
        print('Player o to move.')
        move(turn)
        print_board()

        if win(turn) == True:
            break

        if turn == 9:
            print('Draw.')
            break

main()