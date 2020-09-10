class Solution:
    def minAddToMakeValid(self, S):
        """
        :param S: str
        :return: int
        """
        c = 0
        store = []

        for x in S:
            if x == ')':
                if len(store) > 0 and store[len(store)-1] == '(':
                    del store[len(store)-1]
                else:
                    c += 1
            else:
                store.append('(')

        for x in store:
            c += 1

        return c

