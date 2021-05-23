class Solution:
    def longestStrChain(self, words):
        """
        :param words: List[str]
        :return: int
        """
        ans = 1
        arr = len(words) * [1]
        words.sort(cmp=lambda x,y : len(x) - len(y))


        for i in range(len(words)):
            for j in range(0,i):
                if len(words[i]) == len(words[j]):
                    break

                elif len(words[i])-1 > len(words[j]):
                    continue

                else:
                    if self.Predecessor(words[j], words[i]):
                        arr[i] = max(arr[j]+1, arr[i])
                        ans = max(ans, arr[i])

        return ans


    def Predecessor(self, w1, w2):
        idxW1, idxW2 = 0, 0
        flag1 = False

        while idxW1 < len(w1) and idxW2 < len(w2):

            if w1[idxW1] == w2[idxW2]:
                idxW1 += 1
                idxW2 += 1

            elif flag1 == False:
                idxW2 += 1
                flag1 = True

            else:
                return False

        return True
