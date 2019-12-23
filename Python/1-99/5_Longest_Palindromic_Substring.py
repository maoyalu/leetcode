import unittest


def solution(s):

    # ********** Attempt 2 - 2019/10/08  ********** 

    '''Dynamic Programming'''

    if len(s) < 2:
        return s
    size = len(s)
    dp = [[False for _ in range(size)] for _ in range(size)]
    max_length = 0
    result = ''

    for i in range(size):
        max_length = 1
        dp[i][i] = True
        result = s[i]

    for i in range(size - 1):
        if s[i] == s[i+1]:
            max_length = 2
            dp[i][i+1] = True
            result = s[i:i+2]

    for length in range(2, size):
        for i in range(size - length):
            j = i + length
            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True
                if length + 1 > max_length:
                    max_length = length + 1
                    result = s[i: j+1]
    return result


    # ********** Attempt 1 - 2019/10/08  ********** 
    
    # result = ''
    # for i in range(len(s)):
    #     for j in range(len(s), i, -1):
    #         sub_s = s[i:j]
    #         if sub_s == sub_s[::-1] and len(sub_s) > len(result):
    #             result = sub_s
    # return result



class TestSolution(unittest.TestCase):
    def test1(self):
        s = "babad"
        out = "bab"
        self.assertEqual(solution(s), out)

    def test2(self):
        s = "cbbd"
        out = "bb"
        self.assertEqual(solution(s), out)


if __name__ == "__main__":
    unittest.main()