import unittest


def solution(A):

    # ********** Attempt 1 - 2019/09/20  ********** 

    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


class TestSolution(unittest.TestCase):
    def test1(self):
        A = [[1,2,3],[4,5,6],[7,8,9]]
        answer = [[1,4,7],[2,5,8],[3,6,9]]
        self.assertEqual(solution(A), answer)

    def test2(self):
        A = [[1,2,3],[4,5,6]]
        answer = [[1,4],[2,5],[3,6]]
        self.assertEqual(solution(A), answer)


if __name__ == "__main__":
    unittest.main()