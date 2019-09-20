import unittest


def solution(board):

    # ********** Attempt 1 - 2019/09/20  ********** 

    R = None
    for row in range(8):
        if R is None:
            for colomn in range(8):
                if board[row][colomn] == 'R':
                    R = [row, colomn]
                    break
    target = [None, None, None, None] # up, left, right, down
    for row in range(8):
        if row == R[0]:
            for colomn in range(8):
                if colomn < R[1]:
                    if board[row][colomn] == 'p':
                        target[1] = 1
                    elif board[row][colomn] == 'B':
                        target[1] = 0
                elif colomn > R[1] and target[2] is None:
                    if board[row][colomn] == 'p':
                        target[2] = 1
                    elif board[row][colomn] == 'B':
                        target[2] = 0
        else:
            for colomn in range(8):
                if colomn == R[1]:
                    if row < R[0]:
                        if board[row][colomn] == 'p':
                            target[0] = 1
                        elif board[row][colomn] == 'B':
                            target[0] = 0
                    elif row > R[0] and target[3] is None:
                        if board[row][colomn] == 'p':
                            target[3] = 1
                        elif board[row][colomn] == 'B':
                            target[3] = 0
    for i in range(4):
        if target[i] is None:
            target[i] = 0
    return sum(target)


class TestSolution(unittest.TestCase):
    def test1(self):
        board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
        answer = 3
        self.assertEqual(solution(board), answer)


if __name__ == "__main__":
    unittest.main()