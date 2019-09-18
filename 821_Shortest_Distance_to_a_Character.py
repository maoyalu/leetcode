import unittest


def solution(S, C):

    # ********** Attempt 1 - 2019/09/18  ********** 

    current_index = 0
    next_index = 0
    result = [len(S)] * len(S)
    while next_index < len(S):
        next_index = S[next_index:].find(C)
        if next_index != -1:
            next_index += current_index
            for i in range(len(S)):
                diff = abs(next_index - i)
                if diff < result[i]:
                    result[i] = diff
            next_index += 1
            current_index = next_index
        else:
            break
    return result
        


class TestSolution(unittest.TestCase):
    def test1(self):
        S = "loveleetcode"
        C = "e"
        answer = [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
        self.assertEqual(solution(S, C), answer)


if __name__ == "__main__":
    unittest.main()