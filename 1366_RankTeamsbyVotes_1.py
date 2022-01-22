class Solution:
    def rankTeams(self, votes):
        """
        :param votes: List[str]
        :return: str
        """

        ans = ''
        table  = [[0 for i in range(len(votes[0])+1)] for j in range(26)]

        for x in votes:
            for i,j in enumerate(x):
                table[ord(j)-ord('A')][i] += 1
                table[ord(j)-ord('A')][-1] = ord('Z')-ord(j) + 1

        table.sort(reverse = True)

        for i in range(26):

            if table[i][-1] != 0:
                ans += chr(91 - table[i][-1])

        return ans
