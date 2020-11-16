from collections import Counter
class Solution:
    def canReorderDoubled(self, A):
        """
        :param A: List[int]
        :return: bool
        """
        l = len(A)
        A.sort()
        table = Counter(A)


        for i in range(l):
            if A[i] == 0 or A[i] not in table:
                continue

            elif A[i] > 0:
                if table[2*A[i]] == 0:
                    return False

                else:
                    table[2*A[i]] -= table[A[i]]
                    if table[2*A[i]] == 0:
                        del table[2*A[i]]

                    del table[A[i]]


            else:
                if table[A[i]/2] == 0:
                    return False

                else:
                    table[A[i]/2] -= table[A[i]]

                    if table[A[i]/2] == 0:
                        del table[A[i]/2]

                    del table[A[i]]

        return True
