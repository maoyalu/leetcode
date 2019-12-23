import unittest
import collections


class RecentCounter:

    # ********** Attempt 1 - 2019/09/21  ********** 

    def __init__(self):
        self.pings = collections.deque()

    def ping(self, t):
        self.pings.append(t)
        while t - self.pings[0] > 3000:
            self.pings.popleft()
        return len(self.pings)


class TestRecentCounter(unittest.TestCase):
    def test1(self):
        obj = RecentCounter()
        inputs = [1, 100, 3001, 3002]
        outputs = [1, 2, 3, 3]
        for i in range(len(inputs)):
            self.assertEqual(obj.ping(inputs[i]), outputs[i])


if __name__ == "__main__":
    unittest.main()