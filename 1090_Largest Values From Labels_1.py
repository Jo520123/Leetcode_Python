from collections import defaultdict
class Solution:
    def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
        """
        :param values: List[int]
        :param labels: List[int]
        :param num_wanted: int
        :param use_limit: int
        :return: int
        """
        dic = defaultdict(int)
        ans = 0
        orderByvalue = sorted(zip(values,labels))

        while orderByvalue and num_wanted:
            v, l = orderByvalue.pop()

            if dic[l] < use_limit:
                num_wanted -= 1
                dic[l] += 1
                ans += v

        return ans
