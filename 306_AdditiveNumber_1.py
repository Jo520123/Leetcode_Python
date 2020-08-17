class Solution:
    def isAdditiveNumber(self, num) :
        """
        :param num: str
        :return: bool
        """
        return self.DFS(num, [])

    def DFS(self, num, route):
        if len(route) >= 3 and route[-2]+route[-3] != route[-1]:
            return False

        if len(route) >= 3 and not num:
            return True


        for i in range(len(num)):
            present = num[:i+1]

            if len(present) > 1 and present[0] == '0':
                continue

            if self.DFS(num[i+1:], route + [int(present)]):
                return True

        return False
