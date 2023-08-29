from collections import defaultdict
from collections import Counter

class Solution:
    def findingUsersActiveMinutes(self, logs, k):
        """
        :type logs: List[List[int]]
        :type k: int
        :rtype: List[int]
        """

        idTime = defaultdict(set)

        for x, y in logs:
            idTime[x].add(y)

        count= Counter(len(x) for x in idTime.values())

        ans = []
        for i in range (1, k+1):
            ans.append(count[i])

        return ans