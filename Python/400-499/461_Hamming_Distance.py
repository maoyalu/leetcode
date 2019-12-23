import unittest


def solution(x, y):

    # ********** Attempt 1 - 2019/09/21  ********** 

    count = 0
    while x > 0 or y > 0:
        if x % 2 != y % 2:
            count += 1
        x //= 2
        y //= 2
    return count

class TestSolution(unittest.TestCase):
    def test1(self):
        x = 1
        y = 2
        answer = 2
        self.assertEqual(solution(x, y), answer)


if __name__ == "__main__":
    unittest.main()