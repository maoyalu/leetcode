import unittest


def solution(s):

    # ********** Attempt 1 - 2019/10/31  ********** 

    count = 0
    current = 0
    for c in s:
        if c == "R":
            current += 1
        else:
            current -= 1
        if current == 0:
            count += 1
    return count


class TestSolution(unittest.TestCase):
    def test1(self):
        s = "RLRRLLRLRL"
        out = 4
        self.assertEqual(solution(s), out)

    def test2(self):
        s = "RLLLLRRRLR"
        out = 3
        self.assertEqual(solution(s), out)

    def test3(self):
        s = "LLLLRRRR"
        out = 1
        self.assertEqual(solution(s), out)

    def test4(self):
        s = ""
        out = 0
        self.assertEqual(solution(s), out)


if __name__ == "__main__":
    unittest.main()