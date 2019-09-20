import unittest
from Utils.TreeNode import build_tree_node_from_list, TreeNode


def solution(t1, t2):

    # ********** Attempt 1 - 2019/09/21  ********** 

    if not t1 and not t2:
        return None
    elif not t1:
        return t2
    elif not t2:
        return t1
    root = TreeNode(t1.val + t2.val)
    root.left = solution(t1.left, t2.left)
    root.right = solution(t1.right, t2.right)
    return root


class TestSolution(unittest.TestCase):
    def test1(self):
        t1 = build_tree_node_from_list([1, 3, 2, 5])
        t2 = build_tree_node_from_list([2, 1, 3, None, 4, None, 7])
        answer = build_tree_node_from_list([3, 4, 5, 5, 4, None, 7])
        self.assertEqual(solution(t1, t2), answer)


if __name__ == "__main__":
    unittest.main()