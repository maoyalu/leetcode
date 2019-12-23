import unittest


def solution(A, K):

    # ********** Attempt 2 - 2019/09/20  ********** 

    num = int(''.join(map(str, A))) + K
    return [int(x) for x in str(num)] 

    # ********** Attempt 1 - 2019/09/20  ********** 

    # num = int(''.join([str(x) for x in A])) + K
    # return [int(x) for x in list(str(num))]


class TestSolution(unittest.TestCase):
    def test1(self):
        A = [1,2,0,0]
        K = 34
        answer = [1,2,3,4]
        self.assertEqual(solution(A, K), answer)

    def test2(self):
        A = [2,7,4]
        K = 181
        answer = [4,5,5]
        self.assertEqual(solution(A, K), answer)

    def test3(self):
        A = [2,1,5]
        K = 806
        answer = [1,0,2,1]
        self.assertEqual(solution(A, K), answer)

    def test4(self):
        A = [9,9,9,9,9,9,9,9,9,9]
        K = 1
        answer = [1,0,0,0,0,0,0,0,0,0,0]
        self.assertEqual(solution(A, K), answer)


if __name__ == "__main__":
    unittest.main()