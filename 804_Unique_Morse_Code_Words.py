import unittest


def solution(words):

    # ********** Attempt 1 - 2019/09/20  ********** 

    codelist = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    codes = set()
    for word in words:
        codes.add(''.join([codelist[ord(c) - 97] for c in word]))
    return len(codes)


class TestSolution(unittest.TestCase):
    def test1(self):
        words = ["gin", "zen", "gig", "msg"]
        answer = 2
        self.assertEqual(solution(words), answer)


if __name__ == "__main__":
    unittest.main()