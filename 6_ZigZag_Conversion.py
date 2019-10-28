import unittest


def solution(s, num_rows):

    # ********** Attempt 1 - 2019/10/28  ********** 

    if num_rows == 1 or len(s) <= num_rows:
        return s
    q = [[] for _ in range(num_rows)]
    i = 0
    is_inc = False
    for c in s:
        q[i].append(c)
        if i == num_rows - 1 or i == 0:
            is_inc = not is_inc
        if is_inc:
            i += 1
        else:
            i -= 1
    return ''.join([''.join(x) for x in q])
        


class TestSolution(unittest.TestCase):
    def test1(self):
        s = "PAYPALISHIRING"
        num_rows = 3
        out = "PAHNAPLSIIGYIR"
        self.assertEqual(solution(s, num_rows), out)

    def test2(self):
        s = "PAYPALISHIRING"
        num_rows = 4
        out = "PINALSIGYAHRPI"
        self.assertEqual(solution(s, num_rows), out)

    def test3(self):
        s = "ABC"
        num_rows = 1
        out = "ABC"
        self.assertEqual(solution(s, num_rows), out)


if __name__ == "__main__":
    unittest.main()