import unittest


def solution(s):

    # ********** Attempt 1 - 2019/10/28  ********** 

    symbols = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    length = len(s)
    result = 0
    i = 0
    while i < length:
        if i + 1 < length and symbols[s[i]] < symbols[s[i+1]]:
            result += (symbols[s[i+1]] - symbols[s[i]])
            i += 2
        else:
            result += symbols[s[i]]
            i += 1
    return result


class TestSolution(unittest.TestCase):
    def test1(self):
        s = "III"
        output = 3
        self.assertEqual(solution(s), output)

    def test2(self):
        s = "IV"
        output = 4
        self.assertEqual(solution(s), output)

    def test3(self):
        s = "IX"
        output = 9
        self.assertEqual(solution(s), output)

    def test4(self):
        s = "LVIII"
        output = 58
        self.assertEqual(solution(s), output)

    def test5(self):
        s = "MCMXCIV"
        output = 1994
        self.assertEqual(solution(s), output)


if __name__ == "__main__":
    unittest.main()