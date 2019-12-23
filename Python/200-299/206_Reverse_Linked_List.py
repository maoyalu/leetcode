import unittest
from Utils.ListNode import build_list_node_from_list, ListNode


def solution(head):

    # ********** Attempt 2 - 2019/09/21  ********** 

    current = head
    pre = None
    while current:
        next_node = current.next
        current.next = pre
        pre = current
        current = next_node
    return pre
    
    # ********** Attempt 1 - 2019/09/21  ********** 

    # current = head
    # pre = None
    # while current:
    #     node = ListNode(current.val)
    #     node.next = pre
    #     pre = node
    #     current = current.next
    # return pre


class TestSolution(unittest.TestCase):
    def test1(self):
        head = build_list_node_from_list([1, 2, 3, 4, 5])
        output = build_list_node_from_list([5, 4, 3, 2, 1])
        self.assertEqual(solution(head), output)


if __name__ == "__main__":
    unittest.main()