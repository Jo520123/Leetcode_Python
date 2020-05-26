import sys
class WordDistance:
    def __init__(self,words):
        self.map = {}
        for i in range(len(words)):
            if words[i] in self.map:
                self.map[words[i]].append(i)
            else:
                self.map[words[i]] = [i]

    def shortest(self, x, y):
        idx_t1 = self.map[x]
        idx_t2 = self.map[y]

        idxt1 = 0
        idxt2 = 0
        min_gap = sys.maxsize

        while idxt1 <len(idx_t1) and idxt2 < len(idx_t2):
            min_Diff = min(min_gap, abs(idx_t1[idxt1] - idx_t2[idxt2]))
            if idx_t1[idxt1] < idx_t2[idxt2]:
                idxt1 +=1
            else:
                idxt2 +=1

        return min_gap



