class Solution:
    def reorderLogFiles(self, logs):
        """
        :param logs: List[str]
        :return: List[str]
        """
        not_alp = []
        alp = []
        result = []

        for x in logs:
            x_sep = x.split(" ")
            if x_sep[1].isalpha():
                alp.append((" ".join(x_sep[1:]), x_sep[0]))
            else:
                not_alp.append(x)

        new_apl= sorted(alp)

        for i in new_apl:
            result.append(i[1] +" "+ i[0])

        return result + not_alp
