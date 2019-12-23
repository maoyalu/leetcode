import unittest
from Utils.TreeNode import build_tree_node_from_list


def solution(root, L, R):

    # ********** Attempt 1 - 2019/09/20  ********** 

    sum = 0
    if root:
        if L <= root.val <= R:
            sum += root.val
        if root.val >= L:
            sum += solution(root.left, L, R)
        if root.val <= R:
            sum += solution(root.right, L, R)
    return sum


class TestSolution(unittest.TestCase):
    def test1(self):
        root = build_tree_node_from_list([10,5,15,3,7,None,18])
        L = 7
        R = 15
        answer = 32
        self.assertEqual(solution(root, L, R), answer)

    def test2(self):
        root = build_tree_node_from_list([10,5,15,3,7,13,18,1,None,6])
        L = 6
        R = 10
        answer = 23
        self.assertEqual(solution(root, L, R), answer)


if __name__ == "__main__":
    unittest.main()