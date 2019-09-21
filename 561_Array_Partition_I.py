import unittest


def solution(nums):

    # ********** Attempt 2 - 2019/09/21  **********

    nums.sort()
    return sum(nums[::2])
    
    # ********** Attempt 1 - 2019/09/21  ********** 

    # nums.sort()
    # min_nums = []
    # for i in range(len(nums)):
    #     if i % 2 == 0:
    #         min_nums.append(nums[i])
    # return sum(min_nums)


class TestSolution(unittest.TestCase):
    def test1(self):
        nums = [1, 4, 3, 2]
        answer = 4
        self.assertEqual(solution(nums), answer)


if __name__ == "__main__":
    unittest.main()