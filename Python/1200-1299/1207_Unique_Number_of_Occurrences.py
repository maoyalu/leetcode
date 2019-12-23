import unittest


def solution(arr):

    # ********** Attempt 2 - 2019/10/31  ********** 

    num_dict = {}
    for num in arr:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    count_dict = {}
    for num in num_dict:
        count_dict[num_dict[num]] = num
    return len(num_dict) == len(count_dict)

    
    # ********** Attempt 1 - 2019/10/31  ********** 

    # count = [arr.count(x) for x in set(arr)]
    # return len(count) == len(set(count))


class TestSolution(unittest.TestCase):
    def test1(self):
        arr = [1,2,2,1,1,3]
        self.assertTrue(solution(arr))

    def test2(self):
        arr = [1,2]
        self.assertFalse(solution(arr))

    def test3(self):
        arr = [-3,0,1,-3,1,1,1,-3,10,0]
        self.assertTrue(solution(arr))


if __name__ == "__main__":
    unittest.main()