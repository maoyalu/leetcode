import unittest


def solution(address):

    # ********** Attempt 1 - 2019/09/20  ********** 

    return address.replace(".", "[.]")


class TestSolution(unittest.TestCase):
    def test1(self):
        address = "1.1.1.1"
        answer = "1[.]1[.]1[.]1"
        self.assertEqual(solution(address), answer)

    def test2(self):
        address = "255.100.50.0"
        answer = "255[.]100[.]50[.]0"
        self.assertEqual(solution(address), answer)


if __name__ == "__main__":
    unittest.main()