class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :param s: str
        :return: List[str]
        """
        store = []
        visit = []
        l = len(s)

        for i in range(l):
            subs = s[i:i+10]

            if subs in store:
                visit.append(subs)
            else:
                store.append(subs)

        return list(set(visit))
