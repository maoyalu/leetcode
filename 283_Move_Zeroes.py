import unittest


def solution(nums):

    # ********** Attempt 2 - 2019/09/21  **********

    end = len(nums)
    i = 0
    while i < end:
        if nums[i] == 0:
            nums.append(nums.pop(i))
            end -= 1
        else:
            i += 1

    # ********** Attempt 1 - 2019/09/21  ********** 

    # end = len(nums)
    # i = 0
    # while i < end:
    #     if nums[i] == 0:
    #         for j in range(i + 1, end):
    #             nums[j - 1] = nums[j]
    #         nums[end-1] = 0
    #         end -= 1
    #     else:
    #         i += 1
    

class TestSolution(unittest.TestCase):
    def test1(self):
        nums = [0,1,0,3,12]
        output = [1,3,12,0,0]
        solution(nums)
        self.assertEqual(nums, output)

    def test2(self):
        nums = [0,0,1]
        output = [1,0,0]
        solution(nums)
        self.assertEqual(nums, output)


if __name__ == "__main__":
    unittest.main()