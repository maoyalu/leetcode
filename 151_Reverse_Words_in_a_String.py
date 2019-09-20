import unittest


def solution(s):

    # ********** Attempt 1 - 2019/09/20  ********** 

    li = s.split(' ')
    return ' '.join([ _ for _ in li[::-1] if _ != ''])


class TestSolution(unittest.TestCase):
    def test1(self):
        s = "the sky is blue"
        answer = "blue is sky the"
        self.assertEqual(solution(s), answer)
        
    def test2(self):
        s = "  hello world!  "
        answer = "world! hello"
        self.assertEqual(solution(s), answer)

    def test3(self):
        s = "a good   example"
        answer = "example good a"
        self.assertEqual(solution(s), answer)

if __name__ == "__main__":
    unittest.main()