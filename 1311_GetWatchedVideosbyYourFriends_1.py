from collections import deque
from collections import defaultdict
class Solution:
    def watchedVideosByFriends(self, watchedVideos, friends, id, level):
        """
        :param watchedVideos: List[List[str]]
        :param friends: List[List[int]]
        :param id: int
        :param level: int
        :return: List[str]
        """

        d = defaultdict(list)

        for i, j in enumerate(friends):
            for k in j:
                d[i].append(k)


        curlev, uni, lis = 0, set(), deque()
        lis.append(id)
        uni.add(id)

        while(curlev < level):

            l = len(lis)
            for i in range(l):
                idx = lis.popleft()

                for x in d[idx]:
                    if x not in uni:
                        uni.add(x)
                        lis.append(x)
            curlev += 1

        d2 = defaultdict(int)

        while lis:
            q = lis.popleft()

            for x in watchedVideos[q]:
                d2[x] += 1


        w = sorted((y,x) for x ,y in d2.items())

        ans  = [y for x ,y in w]
        return ans