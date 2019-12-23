import unittest


def solution(S):

    # ********** Attempt 2 - 2019/09/19  **********
    
    if not S:
        return ""
    start = 0
    end = -1
    length = len(S)
    result = []
    while start < length:
        if S[start].isalpha():
            while not S[end].isalpha():
                end -= 1
            result.append(S[end])
            end -= 1
        else:
            result.append(S[start])
        start += 1
    return ''.join(result)
    
    # ********** Attempt 1 - 2019/09/19  ********** 

    # if not S:
    #     return ""
    # start = 0
    # end = -1
    # length = len(S)
    # result = []
    # while start < length:
    #     if 'A' <= S[start] <= 'Z' or 'a' <= S[start] <= 'z':
    #         while not ('A' <= S[end] <= 'Z' or 'a' <= S[end] <= 'z'):
    #             end -= 1
    #         result.append(S[end])
    #         end -= 1
    #     else:
    #         result.append(S[start])
    #     start += 1
    # return ''.join(result)



class TestSolution(unittest.TestCase):
    def test1(self):
        S = "ab-cd"
        answer = "dc-ba"
        self.assertEqual(solution(S), answer)

    def test2(self):
        S = "a-bC-dEf-ghIj"
        answer = "j-Ih-gfE-dCba"
        self.assertEqual(solution(S), answer)

    def test3(self):
        S = "Test1ng-Leet=code-Q!"
        answer = "Qedo1ct-eeLg=ntse-T!"
        self.assertEqual(solution(S), answer)


if __name__ == "__main__":
    unittest.main()