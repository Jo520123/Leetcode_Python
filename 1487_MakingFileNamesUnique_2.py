class Solution:
    def getFolderNames(self, names):
        """
        :param names:  List[str]
        :return: List[str]
        """

        d = {}
        ans = []

        for x in names:

            c = d.get(x,0)

            updateName = x


            if c > 0:

                while updateName in d:

                    updateName = x + "(" +str(c) + ")"

                    c += 1

                d[updateName] = c


            d[updateName] = 1

            ans.append(updateName)



        return ans