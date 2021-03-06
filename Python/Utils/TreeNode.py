class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __eq__(self, node):
        if self and node:
            return self.val == node.val and self.left == node.left and self.right == node.right
        else:
            return False



def build_tree_node_from_list(alist):
    if not alist:
        return None
    root = TreeNode(alist[0])
    queue = [root]
    i = 1
    while i < len(alist) and queue:
        parent = queue.pop(0)
        if not parent:
            i += 2
        else:
            left = None
            right = None
            if alist[i] is not None:
                left = TreeNode(alist[i])
            queue.append(left)
            i += 1
            if i < len(alist):
                if alist[i] is not None:
                    right = TreeNode(alist[i])
                queue.append(right)
                i += 1
            parent.left = left
            parent.right = right
    return root
