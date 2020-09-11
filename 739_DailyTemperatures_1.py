class Solution:
    def dailyTemperatures(self, T):
        """
        :param T: List[int]
        :return: List[int]
        """
        ndays= [0]* len(T)
        s = []

        for i in range(len(T)):
            cur = T[i]
            while len(s) > 0:
                if cur > T[s[-1]]:
                    ndays[s[-1]] = i - s[-1]
                    s.pop()
                else:
                    break

            s.append(i)

        return ndays
