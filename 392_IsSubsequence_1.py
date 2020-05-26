import collections
class Solution:
    def IsSubsequence(self,x,y):
        """
                :type x: str
                :type y: str
                :rtype: bool
                """
        queue = collections.deque(x)
        for c in y:
            if not queue:
                return True
            if c == queue[0]:
                queue.popleft()

        return not queue

