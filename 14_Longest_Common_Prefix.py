import unittest


def solution(strs):

    # ********** Attempt 1 - 2019/10/28  ********** 

    if not strs:
        return ""
    result = []
    i = 0
    length = min([len(x) for x in strs])
    stop = False
    while i < length and not stop:
        current = None
        for s in strs:
            if current is None:
                current = s[i]
            elif s[i] != current:
                stop = True
        if not stop:
            result.append(current)
        i += 1
    return ''.join(result)


class TestSolution(unittest.TestCase):
    def test1(self):
        strs = ["flower","flow","flight"]
        out = "fl"
        self.assertEqual(solution(strs), out)

    def test2(self):
        strs = ["dog","racecar","car"]
        out = ""
        self.assertEqual(solution(strs), out)

    def test3(self):
        strs = []
        out = ""
        self.assertEqual(solution(strs), out)
    


if __name__ == "__main__":
    unittest.main()