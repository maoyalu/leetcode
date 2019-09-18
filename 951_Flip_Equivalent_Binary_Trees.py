import unittest
from Utils.TreeNode import build_tree_node_from_list

def solution(root1, root2):
    if not root1 and not root2:
        return True
    elif not root1 or not root2:
        return False
    else:
        return root1.val == root2.val \
            and ((solution(root1.left, root2.right) \
                    and solution(root1.right, root2.left)) \
                or (solution(root1.left, root2.left) \
                    and solution(root1.right, root2.right)))

class TestSolution(unittest.TestCase):
    def test1(self):
        root1 = build_tree_node_from_list([1,2,3,4,5,6,None,None,None,7,8])
        root2 = build_tree_node_from_list([1,3,2,None,6,4,5,None,None,None,None,8,7])
        self.assertTrue(solution(root1, root2))

if __name__ == "__main__":
    unittest.main()