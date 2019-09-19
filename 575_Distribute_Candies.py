import unittest


def solution(candies):

    # ********** Attempt 1 - 2019/09/19  ********** 
    
    candies_num = len(candies) // 2
    kinds_num = len(set(candies))
    return min(candies_num, kinds_num)


class TestSolution(unittest.TestCase):
    def test1(self):
        candies = [1,1,2,2,3,3]
        answer = 3
        self.assertEqual(solution(candies), answer)

    def test2(self):
        candies = [1,1,2,3]
        answer = 2
        self.assertEqual(solution(candies), answer)


if __name__ == "__main__":
    unittest.main()