import unittest


def solution(n):

    # ********** Attempt 1 - 2019/09/20  ********** 

    result = []
    for i in range(1, n+1):
        string = ""
        if i % 3 == 0:
            string = "Fizz"
        if i % 5 == 0:
            string += "Buzz"
        if not string:
            string = str(i)
        result.append(string)
    return result


class TestSolution(unittest.TestCase):
    def test1(self):
        n = 15
        answer = ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
        self.assertEqual(solution(n), answer)


if __name__ == "__main__":
    unittest.main()