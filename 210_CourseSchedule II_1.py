class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :param numCourses: int
        :param prerequisites: List[List[int]]
        :return: List[int]
        """
        r = set()
        v = set()
        s = []
        self.cycle = False

        List = [[] for i in range(numCourses)]

        for i, j in prerequisites:
            List[j].append(i)

        def DFS(n, v, r, s):
            v.add(n)
            r.add(n)
            for x in List[n]:
                if x in r:
                    self.cycle = True
                if x not in v:
                    DFS(x, v, r, s)

            r.remove(n)
            s.append(n)


        for i in range(numCourses):
            if i not in v:
                DFS(i, v, r, s)

        if self.cycle == True:
            return []

        return s[::-1]
