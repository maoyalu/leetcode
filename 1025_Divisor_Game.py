import unittest


def solution(N):

    # ********** Attempt 1 - 2019/09/19  ********** 

    return N % 2 == 0


class TestSolution(unittest.TestCase):
    def test1(self):
        N = 2
        self.assertTrue(solution(N))

    def test2(self):
        N = 3
        self.assertFalse(solution(N))


if __name__ == "__main__":
    unittest.main()