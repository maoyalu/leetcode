import unittest


def solution(s):

    # ********** Attempt 1 - 2019/10/06  ********** 

    if not s:
        return 0
    start = 0
    end = 1
    max_length = 0
    while end < len(s):
        if s[end] in s[start:end]:
            index = s[start:end].index(s[end]) + start
            if index > start and end - start > max_length:
                max_length = end - start
            start = index + 1
        end +=1
    if end - start > max_length:
        max_length = end - start
    return max_length


class TestSolution(unittest.TestCase):
    def test1(self):
        s = "abcabcbb"
        answer = 3
        self.assertEqual(solution(s), answer)

    def test2(self):
        s = "bbbbb"
        answer = 1
        self.assertEqual(solution(s), answer)

    def test3(self):
        s = "pwwkew"
        answer = 3
        self.assertEqual(solution(s), answer)


if __name__ == "__main__":
    unittest.main()