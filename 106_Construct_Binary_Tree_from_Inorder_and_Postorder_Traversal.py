import unittest
from Utils.TreeNode import build_tree_node_from_list, TreeNode


def solution(inorder, postorder):

    # ********** Attempt 1 - 2019/09/20  ********** 

    if not inorder:
        return None
    root = TreeNode(postorder[-1])
    index = inorder.index(root.val)
    root.left = solution(inorder[:index], postorder[:index])
    root.right = solution(inorder[index+1:], postorder[index:-1])
    return root


class TestSolution(unittest.TestCase):
    def test1(self):
        inorder = [9,3,15,20,7]
        postorder = [9,15,7,20,3]
        root = build_tree_node_from_list([3, 9, 20, None, None, 15, 7])
        self.assertEqual(solution(inorder, postorder), root)


if __name__ == "__main__":
    unittest.main()