class Solution:
    def smallestStringWithSwaps(self, s, pairs):
        """
        :param s: str
        :param pairs:  List[List[int]
        :return: str
        """

        l = len(s)
        lis = list(s)
        v = [False for i in range(l)]
        arr = [[] for i in range(l)]
        ans=""

        def DFS(x):
            v[x] = True
            a.append(x)
            for y in arr[x]:
                if not v[y]:
                    DFS(y)


        for i, j in pairs:
            arr[i].append(j)
            arr[j].append(i)

        for i in range(l):
            if not v[i]:
                a = []
                DFS(i)
                a.sort()
                letter = [lis[x] for x in a]
                letter.sort()

                for i in range(len(a)):
                    lis[a[i]] = letter[i]

        return ans.join(lis)
