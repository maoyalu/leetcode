import unittest
from collections import Counter


def solution(s, t):

    # ********** Attempt 1 - 2019/09/24  ********** 

    count_s = Counter(s)
    count_t = Counter(t)
    return count_s == count_t

    # ********** Attempt 1 - 2019/09/24  ********** 

    # word_dict = {}
    # for c in s:
    #     if c not in word_dict:
    #         word_dict[c] = 1
    #     else:
    #         word_dict[c] += 1
    # for c in t:
    #     if c not in word_dict:
    #         return False
    #     else:
    #         word_dict[c] -= 1
    #         if word_dict[c] < 0:
    #             return False
    # for key in word_dict:
    #     if word_dict[key] != 0:
    #         return False
    # return True


class TestSolution(unittest.TestCase):
    def test1(self):
        s = 'anagram'
        t = 'nagaram'
        self.assertTrue(solution(s, t))

    def test2(self):
        s = 'rat'
        t = 'car'
        self.assertFalse(solution(s, t))


if __name__ == "__main__":
    unittest.main()