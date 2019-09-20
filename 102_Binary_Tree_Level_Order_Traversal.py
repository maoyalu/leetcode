import unittest
from Utils.TreeNode import build_tree_node_from_list


def solution(root):
    
    # ********** Attempt 1 - 2019/09/20  ********** 

    result = []
    q = [root]
    while q:
        current = []
        for i in range(len(q)):
            node = q.pop(0)
            if node:
                current.append(node.val)
                q.append(node.left)
                q.append(node.right)
        if current:
            result.append(current)
    return result


class TestSolution(unittest.TestCase):
    def test1(self):
        root = build_tree_node_from_list([3,9,20,None,None,15,7])
        answer = [[3],[9,20],[15,7]]
        self.assertEqual(solution(root), answer)


if __name__ == "__main__":
    unittest.main()