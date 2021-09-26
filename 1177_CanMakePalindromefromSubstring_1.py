class Solution:
    def canMakePaliQueries(self, s, queries):
        """
        :param s: str
        :param queries: List[List[int]
        :return: List[bool]
        """

        d = {}
        lis=[]
        ans = []

        for x in s:
            d[x] = d.get(x,0)+1
            lis.append(d.copy())

        for i, j, k in queries:
            total = 0

            for m in range(26):
                letter = chr(97+m)
                c = lis[j].get(letter,0)

                if i > 0:
                    c -= lis[i-1].get(letter,0)

                if c % 2 == 1:
                    total += 1

            if (j-i+1) %2 == 1:
                total -= 1

            ans.append(total <= 2*k)

        return ans
