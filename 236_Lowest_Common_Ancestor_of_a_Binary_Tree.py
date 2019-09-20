import unittest
from Utils.TreeNode import build_tree_node_from_list


def solution(root, p, q):

    # ********** Attempt 1 - 2019/09/20  ********** 

    if not root or root in (p, q):
        return root
    left = solution(root.left, p, q)
    right = solution(root.right, p, q)
    if left and right:
        return root
    return left if left else right


class TestSolution(unittest.TestCase):
    def test1(self):
        root = build_tree_node_from_list([3,5,1,6,2,0,8,None,None,7,4])
        p = build_tree_node_from_list([5,6,2,None,None,7,4])
        q = build_tree_node_from_list([1,0,8])
        answer = build_tree_node_from_list([3,5,1,6,2,0,8,None,None,7,4])
        self.assertEqual(solution(root, p, q), answer)

    def test2(self):
        root = build_tree_node_from_list([3,5,1,6,2,0,8,None,None,7,4])
        p = build_tree_node_from_list([5,6,2,None,None,7,4])
        q = build_tree_node_from_list([4])
        answer = build_tree_node_from_list([5,6,2,None,None,7,4])
        self.assertEqual(solution(root, p, q), answer)


if __name__ == "__main__":
    unittest.main()