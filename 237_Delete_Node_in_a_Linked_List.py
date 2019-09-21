import unittest


def solution(node):

    # ********** Attempt 1 - 2019/09/21  ********** 
    node.val = node.next.val
    node.next = node.next.next


class TestSolution(unittest.TestCase):
    def test1(self):
        pass
    

if __name__ == "__main__":
    unittest.main()