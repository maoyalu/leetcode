import unittest

def solution(A, K):

    # ********** Attempt 2 - 2019/09/17  **********

    min_num = min(A)
    max_num = max(A)
    
    result = max_num - min_num - 2 * K
    
    if result > 0:
        return result
    else:
        return 0


    # ********** Attempt 1 - 2019/09/17  **********
       
    # if A:
    #     min = max = A[0]
    #     for i in A:
    #         if i > max:
    #             max = i
    #         elif i < min:
    #             min = i
    #     result = max - min - 2 * K
    #     if result > 0:
    #         return result
    #     else:
    #         return 0
    # else:
    #     return 0

class TestSolution(unittest.TestCase):
    def test1(self):
        A = [1]
        K = 0
        answer = 0
        self.assertEqual(solution(A, K), answer)

    def test2(self):
        A = [0, 10]
        K = 2
        answer = 6
        self.assertEqual(solution(A, K), answer)

    def test3(self):
        A = [1, 3, 6]
        K = 3
        answer = 0
        self.assertEqual(solution(A, K), answer)

if __name__ == "__main__":
    unittest.main()