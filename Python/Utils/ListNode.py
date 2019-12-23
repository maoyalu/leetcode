class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, node):
        return self.val == node.val and self.next == node.next


def build_list_node_from_list(alist):
    if not alist:
        return None
    root = ListNode(alist[0])
    current = root
    i = 1
    while i < len(alist):
        current.next = ListNode(alist[i])
        current = current.next
        i += 1
    return root