# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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

if __name__ == "__main__":
    pass