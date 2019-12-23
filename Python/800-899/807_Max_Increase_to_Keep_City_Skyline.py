import unittest


def solution(grid):

    # ********** Attempt 1 - 2019/09/21  ********** 

    row_max = []
    col_max = []
    row_num = len(grid)
    col_num = len(grid[0])
    for i in range(row_num):
        row_max.append(max(grid[i]))
    for j in range(col_num):
        col_max.append(max([grid[i][j] for i in range(row_num)]))
    result = 0
    for i in range(row_num):
        for j in range(col_num):
            result += (min(row_max[i], col_max[j]) - grid[i][j])
    return result


class TestSolution(unittest.TestCase):
    def test1(self):
        grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
        answer = 35
        self.assertEqual(solution(grid), answer)


if __name__ == "__main__":
    unittest.main()