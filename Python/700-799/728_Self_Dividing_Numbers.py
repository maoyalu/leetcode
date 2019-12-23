import unittest


def solution(left, right):

    # ********** Attempt 1 - 2019/09/21  ********** 
    result = []
    for i in range(left, right + 1):
        div = i
        divisible = True
        while div > 0 and divisible:
            div_next = div // 10
            digit = div - div_next * 10
            if digit == 0:
                divisible = False
            elif i % digit != 0:
                divisible = False
            div = div_next
        if divisible:
            result.append(i)
    return result


class TestSolution(unittest.TestCase):
    def test1(self):
        left = 1
        right = 22
        answer = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
        self.assertEqual(solution(left, right), answer)


if __name__ == "__main__":
    unittest.main()