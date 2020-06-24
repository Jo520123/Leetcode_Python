class Solution:
    def compareVersion(self, version1, version2):
        """
        :param version1: str
        :param version2:  str
        :return: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')

        lg = max(len(v1), len(v2))

        for i in range(lg):
            if i < len(v1):
                vr1 = int(v1[i])
            else:
                vr1 = None

            if i < len(v2):
                vr2 = int(v2[i])
            else:
                vr2 = None

            if not vr2 and vr1:
                return 1

            elif vr2 and not vr1:
                return -1

            elif vr1 and vr2:
                if vr1 > vr2:
                    return 1
                elif vr1 < vr2:
                    return -1
        return 0

