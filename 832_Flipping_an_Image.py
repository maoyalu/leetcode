import unittest


def solution(A):

    # ********** Attempt 1 - 2019/09/20  ********** 

    return [[1-x for x in _[::-1]] for _ in A]


class TestSolution(unittest.TestCase):
    def test1(self):
        A = [[1,1,0],[1,0,1],[0,0,0]]
        answer = [[1,0,0],[0,1,0],[1,1,1]]
        self.assertEqual(solution(A), answer)

    def test2(self):
        A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
        answer = [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
        self.assertEqual(solution(A), answer)


if __name__ == "__main__":
    unittest.main()