import unittest


def solution(letters, target):

    # ********** Attempt 2 - 2019/09/20  ********** 
    letters.sort()
    for c in letters:
        if c > target:
            return c
    return letters[0]

    # ********** Attempt 1 - 2019/09/20  ********** 

    # min_letter = letters[0]
    # result = None

    # for c in letters:
    #     if c < min_letter:
    #         min_letter = c
    #     if c > target and (result is None or c < result):
    #         result = c
    # return result if result else min_letter


class TestSolution(unittest.TestCase):
    def test1(self):
        letters = ["c", "f", "j"]
        target = "a"
        answer = "c"
        self.assertEqual(solution(letters, target), answer)

    def test2(self):
        letters = ["c", "f", "j"]
        target = "c"
        answer = "f"
        self.assertEqual(solution(letters, target), answer)

    def test3(self):
        letters = ["c", "f", "j"]
        target = "d"
        answer = "f"
        self.assertEqual(solution(letters, target), answer)

    def test4(self):
        letters = ["c", "f", "j"]
        target = "g"
        answer = "j"
        self.assertEqual(solution(letters, target), answer)

    def test5(self):
        letters = ["c", "f", "j"]
        target = "j"
        answer = "c"
        self.assertEqual(solution(letters, target), answer)

    def test6(self):
        letters = ["c", "f", "j"]
        target = "k"
        answer = "c"
        self.assertEqual(solution(letters, target), answer)


if __name__ == "__main__":
    unittest.main()