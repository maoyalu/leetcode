import unittest


def solution(n):

    # ********** Attempt 1 - 2020/01/10  ********** 

    productOfDigits = 1
    sumOfDigits = 0
    for digit in str(n):
        productOfDigits *= int(digit)
        sumOfDigits += int(digit)
    return productOfDigits - sumOfDigits


class TestSolution(unittest.TestCase):
    def test1(self):
        n = 234
        out = 14
        self.assertEqual(solution(n), out)

    def test2(self):
        n = 4421
        out = 21
        self.assertEqual(solution(n), out)


if __name__ == "__main__":
    unittest.main()