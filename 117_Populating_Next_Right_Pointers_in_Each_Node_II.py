import unittest


def solution(root):

    # ********** Attempt 1 - 2019/09/20  ********** 

    if not root:
        return None
    
    q = [(1, root)]
    
    while q:
        [level, node] = q.pop(0)
        if q and q[0][0] == level:
            node.next = q[0][1]
        if node.left:
            q.append((level+1, node.left))
        if node.right:
            q.append((level+1, node.right))
    
    return root


class TestSolution(unittest.TestCase):
    def test1(self):
        pass


if __name__ == "__main__":
    unittest.main()