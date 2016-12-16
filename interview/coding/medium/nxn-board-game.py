'''You are given an nxn board in which players place red and black pieces on. When three pieces of the same color
are placed adjacent to each other (horizontally, vertically, or diagonally), the player responsible earns a point.
Given that the board is filled in with 1s and 0s to represent the red and black pieces, create a function to
evaluate the number of points each player has and the winner.'''


def winner(matrix):
    n = len(matrix)
    black, red = 0, 0
    for i in range(n):
        for j in range(n):
            # left
            if i-2 >= 0 and matrix[i-2][j] == matrix[i-1][j] == matrix[i][j]:
                if matrix[i][j] == 0:
                    black += 1
                else:
                    red += 1
            # right
            if i+2 < n and matrix[i][j] == matrix[i+1][j] == matrix[i+2][j]:
                if matrix[i][j] == 0:
                    black += 1
                else:
                    red += 1
            # up
            if j-2 >= 0 and matrix[i][j-2] == matrix[i][j-1] == matrix[i][j]:
                if matrix[i][j] == 0:
                    black += 1
                else:
                    red += 1
            # down
            if j+2 < n and matrix[i][j] == matrix[i][j+1] == matrix[i][j+2]:
                if matrix[i][j] == 0:
                    black += 1
                else:
                    red += 1
            # left-up diagonal
            if i-2 >= 0 and j-2 >= 0 and matrix[i-2][j-2] == matrix[i-1][j-1] == matrix[i][j]:
                if matrix[i][j] == 0:
                    black += 1
                else:
                    red += 1
            # right-up diagonal
            if i+2 < n and j-2 >= 0 and matrix[i][j] == matrix[i+1][j-1] == matrix[i+2][j-2]:
                if matrix[i][j] == 0:
                    black += 1
                else:
                    red += 1
            # right-down diagonal
            if i+2 < n and j+2 < n and matrix[i][j] == matrix[i+1][j+1] == matrix[i+2][j+2]:
                if matrix[i][j] == 0:
                    black += 1
                else:
                    red += 1
            # left-down diagonal
            if i-2 >= 0 and j+2 < n and matrix[i-2][j+2] == matrix[i-1][j+1] == matrix[i][j]:
                if matrix[i][j] == 0:
                    black += 1
                else:
                    red += 1
    red /= 2
    black /= 2
    print("Black: %d\nRed: %d" % (black, red))
    if red > black:
        print("Red is the winner.")
        return 1
    elif red < black:
        print("Black is the winner")
        return 0
    else:
        print("Tie game")
        return -1