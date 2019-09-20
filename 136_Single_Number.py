import unittest


def solution(nums):

    # ********** Attempt 1 - 2019/09/20  ********** 

    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    for n in count.keys():
        if count[n] == 1:
            return n


class TestSolution(unittest.TestCase):
    def test1(self):
        nums = [2, 2, 1]
        answer = 1
        self.assertEqual(solution(nums), answer)

    def test2(self):
        nums = [4, 1, 2, 1, 2]
        answer = 4
        self.assertEqual(solution(nums), answer)


if __name__ == "__main__":
    unittest.main()