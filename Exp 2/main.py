def nqueen (board, pos):
    if pos == len(board):
        return True
    for i in range(len(board)):
        if is_safe(board, pos, i):
            board[pos] = i
            if nqueen(board, pos + 1):
                return True
            board[pos] = 1
    return False

def is_safe(board, pos, i):
    for j in range(pos):
        if board[j] == i or abs(board[j] - i) == abs(j - pos):
            return False
    return True

def main():
    n = int(input())
    board = [1] * n
    print(board)
    nqueen(board, 0)
    for i in range(n):
        print(board[i], end = ' ')
    print()
    print(board)

if __name__ == '__main__':
    main()

# Path: Exp 2/main.py


