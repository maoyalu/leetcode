import unittest
from Utils.TreeNode import build_tree_node_from_list


def solution(root):

    # ********** Attempt 1 - 2019/09/20  ********** 

    def helper(node, result):
        if not node:
            return result
        helper(node.left, result)
        result.append(node.val)
        helper(node.right, result)

    result = []
    helper(root, result)
    return result
        
    


class TestSolution(unittest.TestCase):
    def test1(self):
        root = build_tree_node_from_list([1,None,2, None,None,3])
        answer = [1,3,2]
        self.assertEqual(solution(root), answer)


if __name__ == "__main__":
    unittest.main()