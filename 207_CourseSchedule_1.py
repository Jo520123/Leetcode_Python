from collections import defaultdict
class Solution:
    def canFinish(self, numCourses , prerequisites):
        """
        :param numCourses: int
        :param prerequisites:  List[List[int]]
        :return: bool
        """
        List = defaultdict(list)

        for cur, pre in prerequisites:
            List[pre].append(cur)

        def cycle(i, record, v):
            record[i] = True
            v[i] = True

            for x in List[i]:
                if x not in v and cycle(x, record, v):
                    return True
                elif x in record:
                    return True

            record.pop(i)
            return False

        record = {}
        v = {}

        for i in range(numCourses):
            if i not in v and cycle(i, record, v):
                return False

        return True
