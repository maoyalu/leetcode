import unittest
from Utils.TreeNode import build_tree_node_from_list, TreeNode


def solution(preorder, inorder):

    # ********** Attempt 1 - 2019/09/20  ********** 

    if not preorder:
        return None
    root = TreeNode(preorder[0])
    index = inorder.index(root.val)
    root.left = solution(preorder[1: 1+index], inorder[:index])
    root.right = solution(preorder[1+index:], inorder[index+1:])
    return root


class TestSolution(unittest.TestCase):
    def test1(self):
        preorder = [3,9,20,15,7]
        inorder = [9,3,15,20,7]
        root = build_tree_node_from_list([3, 9, 20, None, None, 15, 7])
        self.assertEqual(solution(preorder, inorder), root)


if __name__ == "__main__":
    unittest.main()