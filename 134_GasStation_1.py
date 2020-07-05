class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :param gas: List[int]
        :param cost: List[int]
        :return: int
        """
        if sum(gas) < sum(cost):
            return -1

        s = 0
        r = 0

        for i in range(len(gas)):
            if gas[i] + r < cost[i]:
                s = i + 1
                r = 0
            else:
                r += gas[i] - cost[i]

        return s
