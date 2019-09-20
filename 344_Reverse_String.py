import unittest


def solution(s):

    # ********** Attempt 1 - 2019/09/20  ********** 

    return s[::-1]


class TestSolution(unittest.TestCase):
    def test1(self):
        s = ["h","e","l","l","o"]
        answer = ["o","l","l","e","h"]
        self.assertEqual(solution(s), answer)

    def test2(self):
        s = ["H","a","n","n","a","h"]
        answer = ["h","a","n","n","a","H"]
        self.assertEqual(solution(s), answer)


if __name__ == "__main__":
    unittest.main()