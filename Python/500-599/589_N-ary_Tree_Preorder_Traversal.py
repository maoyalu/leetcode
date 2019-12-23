import unittest


def solution():

    # ********** Attempt 1 - 2019/10/31  ********** 

    if not root:
        return []
    result = [root.val]
    for child in root.children:
        result += preorder(child)
    return result


class TestSolution(unittest.TestCase):
    def test1(self):
        pass


if __name__ == "__main__":
    unittest.main()