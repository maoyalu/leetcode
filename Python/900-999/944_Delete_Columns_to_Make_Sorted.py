import unittest


def solution(A):

    # ********** Attempt 2 - 2019/09/21  **********
    
    count = 0
    for col in range(len(A[0])):
        temp = [x[col] for x in A]
        if sorted(temp) != temp:
            count += 1
    return count
    
    # ********** Attempt 1 - 2019/09/21  ********** 

    # count = 0
    # word_length = len(A[0])
    # word_count = len(A)
    # for i in range(word_length):
    #     pre = A[0][i]
    #     inc = True
    #     j = 1
    #     while j < word_count and inc:
    #         if A[j][i] < pre:
    #             inc = False
    #             count += 1
    #         else:
    #             pre = A[j][i]
    #         j += 1
    # return count

class TestSolution(unittest.TestCase):
    def test1(self):
        A = ["cba","daf","ghi"]
        answer = 1
        self.assertEqual(solution(A), answer)

    def test2(self):
        A = ["a","b"]
        answer = 0
        self.assertEqual(solution(A), answer)

    def test3(self):
        A = ["zyx","wvu","tsr"]
        answer = 3
        self.assertEqual(solution(A), answer)

    def test4(self):
        A = ["rrjk","furt","guzm"]
        answer = 2
        self.assertEqual(solution(A), answer)


if __name__ == "__main__":
    unittest.main()