import unittest
from Utils.TreeNode import build_tree_node_from_list


def solution(root, sum):

    # ********** Attempt 1 - 2019/09/20  ********** 

    if not root:
        return False
    if not root.left and not root.right:
        return root.val == sum
    else:
        return solution(root.left, sum - root.val) or solution(root.right, sum - root.val)


class TestSolution(unittest.TestCase):
    def test1(self):
        sum = 22
        root = build_tree_node_from_list([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, None, 1])
        self.assertTrue(solution(root, sum))


if __name__ == "__main__":
    unittest.main()