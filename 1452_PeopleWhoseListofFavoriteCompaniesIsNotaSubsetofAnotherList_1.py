class Solution:
    def peopleIndexes(self, favoriteCompanies):
        """
        :param favoriteCompanies: List[List[str]]
        :return: List[int]
        """
        ans = []
        uni = [set(x) for x in favoriteCompanies]
        l = len(favoriteCompanies)


        for i in range(l):
            status = True

            for j in range(l):

                if (i != j):

                    if (uni[i] < uni[j]):

                        status = False
                        break

            if (status):
                ans.append(i)


        return ans
