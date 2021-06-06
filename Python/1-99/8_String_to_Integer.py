import unittest

def solution(s):

    # ********** Attempt 1 - 2021/04/06  ********** 
    
    result = []

    for c in s:
        # Skip leading spaces
        if c == ' ' and not result:
            continue
        # At most one sign and following digits
        elif (c in '+-' and not result) or c.isdigit():
            result.append(c)
        else:
            break
    
    try:
        result = int(''.join(result))
        # Less than -2^31
        if result < -2 ** 31:
            return -2 ** 31
        # Larger than 2^31
        elif result > 2 ** 31 - 1:
            return 2 ** 31 - 1
        # Within range
        else:
            return result
    except:
        # No digits read
        return 0
    

class TestSolution(unittest.TestCase):
    def test1(self):
        s = '42'
        answer = 42
        self.assertEqual(solution(s), answer)

    def test2(self):
        s = '   -42'
        answer = -42
        self.assertEqual(solution(s), answer)
    
    def test3(self):
        s = '4193 with words'
        answer = 4193
        self.assertEqual(solution(s), answer)

    def test4(self):
        s = 'words and 987'
        answer = 0
        self.assertEqual(solution(s), answer)
    
    def test4(self):
        s = '-91283472332'
        answer = -2147483648
        self.assertEqual(solution(s), answer)

    def test5(self):
        s = 'abc'
        answer = 0
        self.assertEqual(solution(s), answer)
        

if __name__ == "__main__":
    unittest.main()