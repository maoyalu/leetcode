import unittest


def solution(A):

    # ********** Attempt 1 - 2019/09/20  ********** 

    A.sort()
    previous = None
    for num in A:
        if num == previous:
            return num
        else:
            previous = num


class TestSolution(unittest.TestCase):
    def test1(self):
        A = [1,2,3,3]
        answer = 3
        self.assertEqual(solution(A), answer)

    def test2(self):
        A = [2,1,2,5,3,2]
        answer = 2
        self.assertEqual(solution(A), answer)

    def test3(self):
        A = [5,1,5,2,5,3,5,4]
        answer = 5
        self.assertEqual(solution(A), answer)


if __name__ == "__main__":
    unittest.main()