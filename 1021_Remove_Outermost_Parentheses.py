import unittest


def solution(S):

    # ********** Attempt 2 - 2019/09/20  **********

    count = 0
    result = ''
    current = 0
    for i in range(len(S)):
        if S[i] == '(':
            count += 1
        else:
            count -= 1
            if count == 0:
                result += S[current + 1: i]
                current = i + 1
    return result


    # ********** Attempt 1 - 2019/09/20  ********** 

    # stack = []
    # result = []
    # for c in S:
    #     if c == "(":
    #         stack.append(c)
    #         if len(stack) > 1:
    #             result.append(c)
    #     else:
    #         stack.pop()
    #         if len(stack) > 0:
    #             result.append(c)
    # return ''.join(result)
        


class TestSolution(unittest.TestCase):
    def test1(self):
        S = "(()())(())"
        answer = "()()()"
        self.assertEqual(solution(S), answer)

    def test2(self):
        S = "(()())(())(()(()))"
        answer = "()()()()(())"
        self.assertEqual(solution(S), answer)

    def test3(self):
        S = "()()"
        answer = ""
        self.assertEqual(solution(S), answer)


if __name__ == "__main__":
    unittest.main()