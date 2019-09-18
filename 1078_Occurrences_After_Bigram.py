import unittest

def solution(text, first, second):

    # ********** Attempt 2 - 2019/09/18  ********** 

    result = []
    words = text.split(" ")
    for i in range(len(words) - 2):
        if words[i] == first and words[i+1] == second:
            result.append(words[i+2])
        i += 1
    return result
    

    # ********** Attempt 1 - 2019/09/18  ********** 

    # result = []
    # words = text.split(" ")
    # if len(words) < 3:
    #     return result
    # else:
    #     i = 0
    #     while i < len(words):
    #         if words[i] == first and (i + 2) < len(words) and words[i + 1] == second:
    #             result.append(words[i + 2])
    #         i += 1
    # return result
    

class TestSolution(unittest.TestCase):
    def test1(self):
        text = "alice is a good girl she is a good student"
        first = "a"
        second = "good"
        answer = ["girl","student"]
        self.assertEqual(solution(text, first, second), answer)

    def test2(self):
        text = "we will we will rock you"
        first = "we"
        second = "will"
        answer = ["we","rock"]
        self.assertEqual(solution(text, first, second), answer)


if __name__ == "__main__":
    unittest.main()