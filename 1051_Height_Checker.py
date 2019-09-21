import unittest


def solution(heights):

    # ********** Attempt 1 - 2019/09/21  ********** 

    temp = sorted(heights)
    count = 0
    for i in range(len(heights)):
        if temp[i] != heights[i]:
            count += 1
    return count


class TestSolution(unittest.TestCase):
    def test1(self):
        input = [1, 1, 4, 2, 1, 3]
        output = 3
        self.assertEqual(solution(input), output)


if __name__ == "__main__":
    unittest.main()