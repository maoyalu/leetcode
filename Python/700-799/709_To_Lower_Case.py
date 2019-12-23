import unittest


def solution(s):

    # ********** Attempt 1 - 2019/09/20  ********** 

    return s.lower()


class TestSolution(unittest.TestCase):
    def test1(self):
        s = "Hello"
        answer = "hello"
        self.assertEqual(solution(s), answer)

    def test2(self):
        s = "here"
        answer = "here"
        self.assertEqual(solution(s), answer)

    def test3(self):
        s = "LOVELY"
        answer = "lovely"
        self.assertEqual(solution(s), answer)


if __name__ == "__main__":
    unittest.main()