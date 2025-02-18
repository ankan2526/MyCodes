# author: ankan2526

import sys,math,heapq,bisect,random
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

ints = lambda : list(map(int,input().split()))
#def gprint(t,ans=''): print(f"Case #{t+1}:",ans)
p = 10**9+7
inf = 10**20+7
#alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#p2 = [1]
#for i in range(70):p2.append(p2[-1]*2)
#ANS=[]


inp = open(r"/Users/ankanmahapatra/Downloads/four_in_a_burrow_input.txt","r")
# inp = open("input.txt", "r")
file = open("fb_output.txt","w")
ANS = ""
I = inp.readlines()
inp = [i.strip() for i in I]

T = int(inp[0])

index = 1


def get_submatrix(grid, r1, r2, c1, c2):
    mat = [[grid[i][j] for j in range(c1, c2+1)] for i in range(r1, r2+1)]
    return mat

def get_winner(board):
    if len(board) == 0:
        return -1
    rows = len(board)
    cols = len(board[0])

    def is_winning_line(cells):
        return len(cells) >= 4 and len(set(cells)) == 1

    # Check horizontal
    for row in range(rows):
        for col in range(cols - 3):
            if is_winning_line(board[row][col:col + 4]):
                return board[row][col]

    # Check vertical
    for col in range(cols):
        for row in range(rows - 3):
            if is_winning_line([board[row + i][col] for i in range(4)]):
                return board[row][col]

    # Check diagonal (top-left to bottom-right)
    for row in range(rows - 3):
        for col in range(cols - 3):
            if is_winning_line([board[row + i][col + i] for i in range(4)]):
                return board[row][col]

    # Check diagonal (bottom-left to top-right)
    for row in range(3, rows):
        for col in range(cols - 3):
            if is_winning_line([board[row - i][col + i] for i in range(4)]):
                return board[row][col]

    return -1



def check_winner(board):
    rows = len(board)
    cols = len(board[0])
    flag = False

    def is_winning_line(cells):
        return len(cells) >= 4 and len(set(cells)) == 1

    # Check horizontal
    for row in range(rows):
        for col in range(cols - 3):
            if is_winning_line(board[row][col:col + 4]):
                winner = board[row][col]
                if get_winner(get_submatrix(board, row+1, 5, col, col+3)) == -1:
                    possible[winner] = 1
                flag = True

    # Check vertical
    for col in range(cols):
        for row in range(rows - 3):
            if is_winning_line([board[row + i][col] for i in range(4)]):
                winner = board[row][col]
                possible[winner] = 1
                flag = True

    # Check diagonal (top-left to bottom-right)
    for row in range(rows - 3):
        for col in range(cols - 3):
            if is_winning_line([board[row + i][col + i] for i in range(4)]):
                winner = board[row][col]
                if get_winner(get_submatrix(board, row+1, 5, col, col+3)) == -1:
                    possible[winner] = 1
                flag = True

    # Check diagonal (bottom-left to top-right)
    for row in range(3, rows):
        for col in range(cols - 3):
            if is_winning_line([board[row - i][col + i] for i in range(4)]):
                winner = board[row][col]
                if get_winner(get_submatrix(board, row-2, 5, col, col+3)) == -1:
                    possible[winner] = 1
                flag = True

    return flag



for t in range(T):
    ANS += f"Case #{t+1}: "
    
    index += 1
    a = []
    for i in range(6):
        b = []
        for j in inp[index]:
            if j == 'F':
                b.append(1)
            else:
                b.append(0)
        a.append(b)
        index += 1
    
    possible = [0, 0]

    if check_winner(board=a) == False:
        ans = "0"
    elif possible[0] == possible[1] == 1:
        ans = "?"
    elif possible[0]:
        ans = "C"
    elif possible[1]:
        ans = "F"
    else:
        ans = "?"
    

    ANS += str(ans) + "\n"


print(ANS[:700])
file.write(ANS)
file.close()
