class Solution:
    def findRestaurant(self, list1, list2):
        """
        :param list1: List[str]
        :param list2: List[str]
        :return: List[str]
        """
        table1 = dict()
        table2 = dict()
        low_idx = float("inf")
        result = []

        for i,j in enumerate(list1):
            table1[j] = i

        for i, j in enumerate(list2):
            table2[j] = i


        for x in table1:
            if x in table2:
                sum_idx = table1[x] + table2[x]

                if low_idx > sum_idx:
                    low_idx = sum_idx
                    result = [x]

                elif low_idx == sum_idx:
                    result.append(x)

        return result
