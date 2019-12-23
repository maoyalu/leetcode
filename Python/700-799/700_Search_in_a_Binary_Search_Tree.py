import unittest
from Utils.TreeNode import build_tree_node_from_list


def solution(root, val):

    # ********** Attempt 2 - 2019/09/21  ********** 

    if not root:
        return None
    if root.val == val:
        return root
    elif root.val > val:
        return solution(root.left, val)
    else:
        return solution(root.right, val)

    # ********** Attempt 1 - 2019/09/21  ********** 

    # if not root:
    #     return None
    # if root.val == val:
    #     return root
    # if root.left:
    #     left = solution(root.left, val)
    #     if left:
    #         return left
    # if root.right:
    #     right = solution(root.right, val)
    #     if right:
    #         return right


class TestSolution(unittest.TestCase):
    def test1(self):
        root = build_tree_node_from_list([4, 2, 7, 1, 3])
        val = 2
        answer = build_tree_node_from_list([2, 1, 3])
        self.assertEqual(solution(root, val), answer)

    def test2(self):
        root = build_tree_node_from_list([4, 2, 7, 1, 3])
        val = 5
        answer = None
        self.assertEqual(solution(root, val), answer)


if __name__ == "__main__":
    unittest.main()