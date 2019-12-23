import unittest


def solution(nums, target):

    # ********** Attempt 1 - 2019/03/04  ********** 

    size = len(nums)
    dist = {}

    for i in range(size):
        dist[target - nums[i]] = i
    for i in range(size):
        if nums[i] in dist and dist[nums[i]] != i:
            return [i, dist[nums[i]]]


class TestSolution(unittest.TestCase):
    def test1(self):
        nums = [2, 7, 11, 15]
        target = 9
        answer = [0, 1]
        self.assertEqual(solution(nums, target), answer)

    def test2(self):
        nums = [3, 2, 4]
        target = 6
        answer = [1, 2]
        self.assertEqual(solution(nums, target), answer)


if __name__ == "__main__":
    unittest.main()