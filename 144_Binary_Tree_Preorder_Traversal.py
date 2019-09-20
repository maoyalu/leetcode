import unittest
from Utils.TreeNode import build_tree_node_from_list


def solution(root):

    # ********** Attempt 1 - 2019/09/20  ********** 

    result = []
    if not root:
        return result
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result


class TestSolution(unittest.TestCase):
    def test1(self):
        root = build_tree_node_from_list([1,None,2,None,None,3])
        answer = [1,2,3]
        self.assertEqual(solution(root), answer)


if __name__ == "__main__":
    unittest.main()