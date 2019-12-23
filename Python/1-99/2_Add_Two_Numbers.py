import unittest
from Utils.ListNode import build_list_node_from_list, ListNode


def solution(l1, l2):

    # ********** Attempt 2 - 2019/10/05  ********** 

    s1 = []
    while l1:
        s1.append(l1.val)
        l1 = l1.next
    num1 = ''.join(map(str, s1[::-1]))
    s2 = []
    while l2:
        s2.append(str(l2.val))
        l2 = l2.next
    num2 = ''.join(map(str, s2[::-1]))
    result = str(int(num1) + int(num2))
    root = ListNode(int(result[-1]))
    current = root
    for digit in result[-2::-1]:
        current.next = ListNode(int(digit))
        current = current.next
    return root


    # ********** Attempt 1 - 2019/10/05  ********** 

    # current_node_1 = l1
    # current_node_2 = l2
    # root = None
    # current_root = None
    # inc = 0
    # while current_node_1 or current_node_2 or inc:
    #     val = inc
    #     if current_node_1:
    #         val += current_node_1.val
    #         current_node_1 = current_node_1.next
    #     if current_node_2:
    #         val += current_node_2.val
    #         current_node_2 = current_node_2.next
    #     inc = val // 10
    #     val = val % 10
    #     if not root:
    #         root = ListNode(val)
    #         current_root = root
    #     else:
    #         node = ListNode(val)
    #         current_root.next = node
    #         current_root = node
    # return root
    

class TestSolution(unittest.TestCase):
    def test1(self):
        in1 = build_list_node_from_list([2, 4, 3])
        in2 = build_list_node_from_list([5, 6, 4])
        out = build_list_node_from_list([7, 0, 8])
        self.assertEqual(solution(in1, in2), out)

    def test2(self):
        in1 = build_list_node_from_list([6, 1, 8, 9])
        in2 = build_list_node_from_list([7, 3, 6])
        out = build_list_node_from_list([3, 5, 4, 0, 1])
        self.assertEqual(solution(in1, in2), out)

    def test3(self):
        in1 = build_list_node_from_list([0])
        in2 = build_list_node_from_list([7, 3, 6])
        out = build_list_node_from_list([7, 3, 6])
        self.assertEqual(solution(in1, in2), out)


if __name__ == "__main__":
    unittest.main()