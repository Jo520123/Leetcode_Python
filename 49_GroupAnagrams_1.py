class Solution:
    def groupAnagrams(self, strs):
        """
        :param strs:  List[str]
        :return: List[List[str]]
        """
        result={}
        l = len(strs)
        if l < 1:
            return strs
        else:
            for i in range(l):
                org = strs[i]
                org_sort = "".join(sorted(org))
                if org_sort in result:
                    result[org_sort].append(org)
                else:
                    result[org_sort] = [org]

        return result.values()
