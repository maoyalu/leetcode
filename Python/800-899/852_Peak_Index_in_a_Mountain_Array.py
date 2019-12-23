import unittest


def solution(A):

    # ********** Attempt 1 - 2019/09/20  ********** 

    start = 0
    end = len(A) - 1
    while start + 1 < end:
        mid = (start + end) // 2
        if A[mid-1] < A[mid] and A[mid+1] < A[mid]:
            return mid
        elif A[mid-1] < A[mid]:
            start = mid
        else:
            end = mid
    return end


class TestSolution(unittest.TestCase):
    def test1(self):
        A = [0,1,0]
        answer = 1
        self.assertEqual(solution(A), answer)

    def test2(self):
        A = [0,2,1,0]
        answer = 1
        self.assertEqual(solution(A), answer)


if __name__ == "__main__":
    unittest.main()