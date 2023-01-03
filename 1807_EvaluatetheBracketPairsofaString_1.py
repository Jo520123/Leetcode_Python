class Solution:
    def evaluate(self, s, knowledge):
        """
        :param s: str
        :param knowledge: List[List[str]]
        :return:str
        """

        d = {}
        l = len(knowledge)

        for i in range(l):
            d[knowledge[i][0]] = knowledge[i][1]

        ls = len(s)
        ans = ""
        ts = ""
        i = 0

        while i < ls:

            if s[i] == "(":
                i += 1

                while i < ls and s[i] != ")":
                    ts += s[i]
                    i += 1

                if ts in d:
                    ans += d[ts]

                else:
                    ans += "?"

            else:
                ans += s[i]

            ts = ""
            i += 1

        return ans
