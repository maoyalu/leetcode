import unittest


def solution(x):

    # ********** Attempt 1 - 2019/10/28  ********** 

    s = str(x)
    return s == s[::-1]


class TestSolution(unittest.TestCase):
    def test1(self):
        input = 121
        output = True
        self.assertEqual(solution(input), output)
    
    def test2(self):
        input = -121
        output = False
        self.assertEqual(solution(input), output)

    def test3(self):
        input = 10
        output = False
        self.assertEqual(solution(input), output)



if __name__ == "__main__":
    unittest.main()