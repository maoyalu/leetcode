import unittest


def solution(x):

    # ********** Attempt 1 - 2019/09/20  ********** 

    result = int(str(x)[::-1]) if x > 0 else -int(str(-x)[::-1])
    return 0 if result > 2 ** 31 - 1 or result < -2 ** 31 else result


class TestSolution(unittest.TestCase):
    def test1(self):
        x = 123
        answer = 321
        self.assertEqual(solution(x), answer)

    def test2(self):
        x = -123
        answer = -321
        self.assertEqual(solution(x), answer)

    def test3(self):
        x = 120
        answer = 21
        self.assertEqual(solution(x), answer)

    def test4(self):
        x = 1463847413
        answer = 0
        self.assertEqual(solution(x), answer)

    def test5(self):
        x = -1463847413
        answer = 0
        self.assertEqual(solution(x), answer)


if __name__ == "__main__":
    unittest.main()