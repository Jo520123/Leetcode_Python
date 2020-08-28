from collections import Counter
class Solution:
    def generatePalindromes(self, s):
        """
        :param s: str
        :return: List[str]
        """
        count = Counter(s)
        center = ""
        rem = ""

        for x, y in count.items():
            if y % 2 == 1:
                center += x
            else:
                rem += (x*(y//2))


        if len(center) < 2:
            return self.permutate(center, rem)
        else:
            return []


    def permutate(self, center, rem):
        visit = [0]*len(rem)
        ans = []
        self.DFS(center, rem, ans, visit, [])
        return ans


    def DFS(self, center, rem, ans, visit, route):
        if len(rem) == len(route):
            f_half = ''.join(route)
            whole = f_half + center +f_half[::-1]
            ans.append(whole)
            return

        for i in range(len(rem)):
            if not visit[i] and not (i>1 and rem[i-1] == rem[i] and visit[i-1]):
                visit[i] = 1
                route.append(rem[i])
                self.DFS(center, rem, ans, visit, route)
                route.pop()
                visit[i] = 0
