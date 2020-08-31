import itertools
class Solution:
    def expand(self, S):
        """
        :param S: str
        :return: List[str]
        """
        lis = []
        c = 0

        for x in S:
            if x == "{":
                c += 1
                lis.append([])
            elif x == "}":
                c -= 1
            elif x == ",":
                continue
            else:
                if c == 1:
                    lis[-1].append(x)
                else:
                    lis.append([x])

        temp = map(''.join, (itertools.product(*lis)))

        return list(temp)
