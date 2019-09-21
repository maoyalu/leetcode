import unittest


def solution(nums):

    # ********** Attempt 1 - 2019/09/21  ********** 

    length = len(nums)
    num_dict = {}
    for num in nums:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
        if num_dict[num] > length / 2:
            return num


class TestSolution(unittest.TestCase):
    def test1(self):
        nums = [3,2,3]
        output = 3
        self.assertEqual(solution(nums), output)

    def test2(self):
        nums = [2,2,1,1,1,2,2]
        output = 2
        self.assertEqual(solution(nums), output)


if __name__ == "__main__":
    unittest.main()