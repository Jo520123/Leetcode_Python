class Solution:
    def topKFrequent(self, nums, k):
        """
        :param nums: List[int]
        :param k: int
        :return: List[int]
        """
        ans = []
        table = {}

        for x in nums:
            if x in table:
                table[x] += 1
            else:
                table[x] = 1

        table_key = list(table.keys())
        table_val = list(table.values())

        table_sort_val = sorted(table.values(), reverse = True)

        visit = []
        c = 0

        for x in table_sort_val:
            if table_key[table_val.index(x)] not in visit:
                ans.append(table_key[table_val.index(x)])
                visit.append(table_key[table_val.index(x)])

            else:
                for k,v in table.items():
                    if v == x and k not in visit :
                        ans.append(k)

            c += 1
            if c == k:
                break


        return ans
