import unittest


def solution(S):

    # ********** Attempt 1 - 2019/09/20  ********** 

    size = len(S)
    indexes = [0]
    index = 1
    for c in S:
        if c == "I":
            indexes.append(index)
        else:
            indexes.insert(0, index)
        index += 1
    result = [None for i in range(size+1)]
    A = [x for x in range(size+1)]
    for i in range(size+1):
        result[indexes[i]] = A[i]
    return result


class TestSolution(unittest.TestCase):
    def test1(self):
        S = "IDID"
        self.assertTrue(self._testResult(S, solution(S)))

    def test2(self):
        S = "III"
        self.assertTrue(self._testResult(S, solution(S)))

    def test3(self):
        S = "DDI"
        self.assertTrue(self._testResult(S, solution(S)))

    def _testResult(self, S, A):
        i = 0
        result = True
        for opt in S:
            if opt == 'I':
                if not (A[i] < A[i+1]):
                    result = False
                    break
            else:
                if not (A[i] > A[i+1]):
                    result = False
                    break
            i += 1
        return result


if __name__ == "__main__":
    unittest.main()