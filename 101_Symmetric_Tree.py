import unittest
from Utils.TreeNode import build_tree_node_from_list


def solution(root):

    # ********** Attempt 1 - 2019/09/20  ********** 
    
    def helper(left, right):
        if left and right:
            return left.val == right.val and helper(left.left, right.right) and helper(left.right, right.left)
        elif not left and not right:
            return True
        else:
            return False
    
    if not root:
        return True
    return helper(root.left, root.right)
        

class TestSolution(unittest.TestCase):
    def test1(self):
        root = build_tree_node_from_list([1,2,2,3,4,4,3])
        self.assertTrue(solution(root))

    def test2(self):
        root = build_tree_node_from_list([1,2,2,None,3,None,3])
        self.assertFalse(solution(root))


if __name__ == "__main__":
    unittest.main()