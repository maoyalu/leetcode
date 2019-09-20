import unittest


def solution(J, S):

    # ********** Attempt 1 - 2019/09/20  ********** 

    return sum([S.count(x) for x in J])


class TestSolution(unittest.TestCase):
    def test1(self):
        J = "aA"
        S = "aAAbbbb"
        answer = 3
        self.assertEqual(solution(J, S), answer)

    def test2(self):
        J = "z"
        S = "ZZ"
        answer = 0
        self.assertEqual(solution(J, S), answer)


if __name__ == "__main__":
    unittest.main()