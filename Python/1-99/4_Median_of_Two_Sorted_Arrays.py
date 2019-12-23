import unittest


def solution(nums1, nums2):

    # ********** Attempt 1 - 2019/10/07  ********** 

    nums = sorted(nums1 + nums2)
    mid = len(nums) // 2
    if len(nums) % 2 == 0:
        return (nums[mid - 1] + nums[mid]) / 2
    else:
        return nums[mid]



class TestSolution(unittest.TestCase):
    def test1(self):
        nums1 = [1, 3]
        nums2 = [2]
        median = 2.0
        self.assertEqual(solution(nums1, nums2), median)

    def test2(self):
        nums1 = [1, 2]
        nums2 = [3, 4]
        median = 2.5
        self.assertEqual(solution(nums1, nums2), median)

    def test3(self):
        nums1 = [1, 2]
        nums2 = []
        median = 1.5
        self.assertEqual(solution(nums1, nums2), median)

    def test4(self):
        nums1 = [1, 2, 3]
        nums2 = []
        median = 2
        self.assertEqual(solution(nums1, nums2), median)

    def test5(self):
        nums1 = [1]
        nums2 = []
        median = 1
        self.assertEqual(solution(nums1, nums2), median)

    def test6(self):
        nums1 = []
        nums2 = [1, 2]
        median = 1.5
        self.assertEqual(solution(nums1, nums2), median)

    def test7(self):
        nums1 = []
        nums2 = [1, 2, 3]
        median = 2
        self.assertEqual(solution(nums1, nums2), median)

    def test8(self):
        nums1 = []
        nums2 = [1]
        median = 1
        self.assertEqual(solution(nums1, nums2), median)


if __name__ == "__main__":
    unittest.main()