import unittest


def solution(grid):

    # ********** Attempt 2 - 2019/09/19  ********** 
    
    area = 0
    N = len(grid)
    for i in range(N):
        for j in range(N):
            if grid[i][j]:
                area += (2 + 4 * grid[i][j])
            if i:
                area -= min(grid[i - 1][j], grid[i][j]) * 2
            if j:
                area -= min(grid[i][j - 1], grid[i][j]) * 2
    return area

    # ********** Attempt 1 - 2019/09/19  ********** 

    # if not grid:
    #     return 0

    # area = 0
    # N = len(grid)
    # for i in range(N):
    #     for j in range(N):
    #         if grid[i][j] != 0:
    #             area += 2

    #         if i <= 0:
    #             area += grid[i][j]
    #         elif grid[i-1][j] < grid[i][j]:
    #             area += (grid[i][j] - grid[i - 1][j])

    #         if j <= 0:
    #             area += grid[i][j]
    #         elif grid[i][j - 1] < grid[i][j]:
    #             area += (grid[i][j] - grid[i][j - 1])

    #         if i + 1 >=  N:
    #             area += grid[i][j]
    #         elif grid[i + 1][j] < grid[i][j]:
    #             area += (grid[i][j] - grid[i + 1][j])

    #         if j + 1 >= N:
    #             area += grid[i][j]
    #         elif grid[i][j + 1] < grid[i][j]:
    #             area += (grid[i][j] - grid[i][j + 1])
    # return area


class TestSolution(unittest.TestCase):
    def test1(self):
        grid = [[2]]
        answer = 10
        self.assertEqual(solution(grid), answer)

    def test2(self):
        grid = [[1,2],[3,4]]
        answer = 34
        self.assertEqual(solution(grid), answer)

    def test3(self):
        grid = [[1,0],[0,2]]
        answer = 16
        self.assertEqual(solution(grid), answer)

    def test4(self):
        grid = [[1,1,1],[1,0,1],[1,1,1]]
        answer = 32
        self.assertEqual(solution(grid), answer)

    def test5(self):
        grid = [[2,2,2],[2,1,2],[2,2,2]]
        answer = 46
        self.assertEqual(solution(grid), answer)


if __name__ == "__main__":
    unittest.main()