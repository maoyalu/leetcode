import unittest
from Utils.TreeNode import build_tree_node_from_list


def solution(root):

    # ********** Attempt 2 - 2019/09/20  ********** 

    current_lvl = [root]
    result = []
    while current_lvl:
        vals = [node.val for node in current_lvl]
        next_lvl = [node for parent in current_lvl for node in [parent.left, parent.right] if node is not None]
        result.append(sum(vals) / len(vals))
        current_lvl = next_lvl
    return result

    
    # ********** Attempt 1 - 2019/09/20  ********** 

    # current_lvl = 1
    # queue = [(root, current_lvl)]
    # result = []
    # total = 0
    # count = 0
    # while queue:
    #     node, lvl = queue.pop(0)
    #     if lvl == current_lvl:
    #         total += node.val
    #         count += 1
    #     else:
    #         result.append(total / count)
    #         total = node.val
    #         count = 1
    #         current_lvl += 1
    #     if node.left:
    #         queue.append((node.left, current_lvl + 1))
    #     if node.right:
    #         queue.append((node.right, current_lvl + 1))
    # result.append(total / count)
    # return result


class TestSolution(unittest.TestCase):
    def test1(self):
        tree = build_tree_node_from_list([3, 9, 20, None, None, 15, 7])
        answer = [3, 14.5, 11]
        self.assertEqual(solution(tree), answer)

    def test2(self):
        tree = build_tree_node_from_list([3, 9, 20, 15, 7])
        answer = [3, 14.5, 11]
        self.assertEqual(solution(tree), answer)


if __name__ == "__main__":
    unittest.main()