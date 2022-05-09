class Solution:
    def getFolderNames(self, names):
        """
        :param names:  List[str]
        :return: List[str]
        """

        d = {}
        ans = []

        for x in names:
            if x not in d:

                ans.append(x)

                d[x] = True

            else:
                for i in range(1, 999999):
                    updateName = x +"("+str(i)+")"

                    if updateName not in d:

                        ans.append(updateName)

                        d[updateName] = True

                        break


        return ans