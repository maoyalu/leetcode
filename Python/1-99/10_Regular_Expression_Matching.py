import unittest

def solution(s, p):

    # ********** Attempt 1 - 2021/04/06  ********** 

    m = len(s)
    n = len(p)
    dp = [[None for _ in range(n+1)] for _ in range(m+1)]

    # Iterate through s
    for i in range(m+1):
        # Iterate through p
        for j in range(n+1):
            # Both s and p are empty
            if(i == 0 and j == 0):
                dp[i][j] = True
            # s is empty
            elif i == 0:
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-2]
                else:    
                    dp[i][j] = False
            # p is empty
            elif j == 0:
                dp[i][j] = False
            else:
                if p[j-1] == '*':
                    # For 0 time
                    dp[i][j] = dp[i][j-2]
                    # For 1 time
                    if p[j-2] == '.' or p[j-2] == s[i-1]:
                        dp[i][j] = dp[i-1][j] or dp[i][j]
                elif s[i-1] == p[j-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = False
    return dp[m][n]


class TestSolution(unittest.TestCase):
    def test1(self):
        s = 'aa'
        p = 'a'
        self.assertFalse(solution(s, p))

    def test2(self):
        s = 'aa'
        p = 'a*'
        self.assertTrue(solution(s, p))

    def test3(self):
        s = 'ab'
        p = '.*'
        self.assertTrue(solution(s, p))

    def test4(self):
        s = 'aab'
        p = 'c*a*b'
        self.assertTrue(solution(s, p))

    def test5(self):
        s = 'mississippi'
        p = 'mis*is*p*.'
        self.assertFalse(solution(s, p))

    def test6(self):
        s = ''
        p = ''
        self.assertTrue(solution(s, p))

    def test7(self):
        s = 'aaa'
        p = 'a*a'
        self.assertTrue(solution(s, p))
    
    def test8(self):
        s = 'mississippi'
        p = 'mis*is*ip*.'
        self.assertTrue(solution(s, p))

    def test9(self):
        s = 'aaa'
        p = 'ab*a*c*a'
        self.assertTrue(solution(s, p))

    def test10(self):
        s = ''
        p = 'a*'
        self.assertTrue(solution(s, p))
        

if __name__ == "__main__":
    unittest.main()