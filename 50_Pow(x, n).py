import unittest


def solution(x, n):

    # ********** Attempt 1 - 2019/10/31  ********** 

    return x ** n


class TestSolution(unittest.TestCase):
    def test1(self):
        x = 2.00000
        n = 10
        out = 1024.00000
        self.assertEqual(solution(x, n), out)

    def test2(self):
        x = 2.10000
        n = 3
        out = 9.26100
        self.assertEqual(solution(x, n), out)

    def test3(self):
        x = 2.00000
        n = -2
        out = 0.25000
        self.assertEqual(solution(x, n), out)


if __name__ == "__main__":
    unittest.main()