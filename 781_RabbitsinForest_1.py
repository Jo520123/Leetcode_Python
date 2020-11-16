from collections import Counter
import math
class Solution:
    def numRabbits(self, answers):
        """
        :param answers: List[int]
        :return: int
        """
        if len(answers) == 0:
            return 0

        ans = []
        table = Counter(answers)

        for k in table:
            ans.append((table[k]+k)//(k+1)*(k+1))


        return sum(ans)
