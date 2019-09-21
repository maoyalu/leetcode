import unittest
from Utils.TreeNode import build_tree_node_from_list


def solution(root):

    # ********** Attempt 1 - 2019/09/21  ********** 

    def helper(root, sum):
        if not root:
            return 0
        if root.right:
            sum = helper(root.right, sum)
        root.val += sum
        sum = root.val
        if root.left:
            sum = helper(root.left, sum)
        return sum
    
    helper(root, 0)
    return root
    

class TestSolution(unittest.TestCase):
    def test1(self):
        root = build_tree_node_from_list([4,1,6,0,2,5,7,None,None,None,3,None,None,None,8])
        answer = build_tree_node_from_list([30,36,21,36,35,26,15,None,None,None,33,None,None,None,8])
        self.assertEqual(solution(root), answer)


if __name__ == "__main__":
    unittest.main()