import unittest


def solution(A):

    # ********** Attempt 1 - 2019/09/20  ********** 

    start = 0
    end = len(A) - 1
    while start < end:
        while A[start] % 2 == 0 and start < end:
            start += 1
        while A[end] % 2 != 0 and start < end:
            end -= 1
        A[start], A[end] = A[end], A[start]
        end -= 1
    return A


class TestSolution(unittest.TestCase):
    def test1(self):
        A = [3,1,2,4]
        answer = [4,2,1,3]
        self.assertEqual(solution(A), answer)


if __name__ == "__main__":
    unittest.main()