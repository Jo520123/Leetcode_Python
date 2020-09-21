class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :param s: str
        :return: List[str]
        """
        store = set()
        visit = set()
        l = len(s)

        for i in range(l):
            subs = s[i:i + 10]

            if subs in store:
                visit.add(subs)

            else:
                store.add(subs)


        return list(visit)
