import unittest


def solution(A):

    # ********** Attempt 1 - 2019/09/19  ********** 

    each = sum(A) / 3
    i = 0
    sum1 = 0
    while i < len(A):
        sum1 += A[i]
        if sum1 == each:
            j = i + 1
            sum2 = 0
            while j < len(A):
                sum2 += A[j]
                if sum2 == each:
                    return True
                j += 1
        i += 1
    return False



class TestSolution(unittest.TestCase):
    def test1(self):
        A = [0,2,1,-6,6,-7,9,1,2,0,1]
        self.assertTrue(solution(A))

    def test2(self):
        A = [0,2,1,-6,6,7,9,-1,2,0,1]
        self.assertFalse(solution(A))

    def test3(self):
        A = [3,3,6,5,-2,2,5,1,-9,4]
        self.assertTrue(solution(A))


if __name__ == "__main__":
    unittest.main()