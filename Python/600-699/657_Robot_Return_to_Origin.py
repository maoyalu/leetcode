import unittest


def solution(moves):

    # ********** Attempt 1 - 2019/09/20  ********** 

    return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")


class TestSolution(unittest.TestCase):
    def test1(self):
        moves = "UD"
        self.assertTrue(solution(moves))

    def test2(self):
        moves = "LL"
        self.assertFalse(solution(moves))


if __name__ == "__main__":
    unittest.main()