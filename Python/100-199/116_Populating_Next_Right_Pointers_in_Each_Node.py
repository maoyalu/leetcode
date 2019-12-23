import unittest


def solution(root):

    # ********** Attempt 1 - 2019/09/20  ********** 

    if not root:
        return None
    
    if root.left:
        root.left.next = root.right
        
    if root.right and root.next:
        root.right.next = root.next.left
        
    solution(root.left)
    solution(root.right)
    
    return root


class TestSolution(unittest.TestCase):
    def test1(self):
        pass


if __name__ == "__main__":
    unittest.main()