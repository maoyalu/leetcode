import unittest


def solution(A):

    # ********** Attempt 1 - 2019/09/20  ********** 

    result = [x**2 for x in A]
    result.sort()
    return result


class TestSolution(unittest.TestCase):
    def test1(self):
        A = [-4,-1,0,3,10]
        answer = [0,1,9,16,100]
        self.assertEqual(solution(A), answer)
    
    def test2(self):
        A = [-7,-3,2,3,11]
        answer = [4,9,9,49,121]
        self.assertEqual(solution(A), answer)


if __name__ == "__main__":
    unittest.main()