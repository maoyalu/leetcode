import unittest
from Utils.TreeNode import build_tree_node_from_list


def solution(root):

    # ********** Attempt 1 - 2019/09/20  ********** 

    if not root:
        return 0
    return max(solution(root.left), solution(root.right)) + 1


class TestSolution(unittest.TestCase):
    def test1(self):
        root = build_tree_node_from_list([3,9,20,None,None,15,7])
        answer = 3
        self.assertEqual(solution(root), answer)


if __name__ == "__main__":
    unittest.main()