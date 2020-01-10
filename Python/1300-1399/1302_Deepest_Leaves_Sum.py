import unittest

# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def solution(root):

    # ********** Attempt 1 - 2020/01/10  ********** 

    # if not root:
    #     return 0
    
    # def expand_next_level_helper(nodes):
    #     next_level = []
    #     for node in nodes:
    #         if node.left:
    #             next_level.append(node.left)
    #         if node.right:
    #             next_level.append(node.right)
    #     return next_level
        
    # q = [root]
    # next_q = expand_next_level_helper(q)
    # while next_q:
    #     q = next_q
    #     next_q = expand_next_level_helper(q)
    # return sum([node.val for node in q])


    # ********** Attempt 2 - 2020/01/10  ********** 

    current_level = [root]
    pre_level = []
    while current_level:
        pre_level = current_level
        current_level = [child for node in current_level for child in [node.left, node.right] if child]
    return sum([node.val for node in pre_level])



class TestSolution(unittest.TestCase):
    def test1(self):
        n = 234
        out = 14
        self.assertEqual(solution(n), out)

    def test2(self):
        n = 4421
        out = 21
        self.assertEqual(solution(n), out)


if __name__ == "__main__":
    unittest.main()