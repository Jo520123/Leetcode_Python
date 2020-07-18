class Solution:
    def findWords(self, words):
        """
        :param words: List[str]
        :return: List[str]
        """
        row1 = ['q', 'w','e','r','t','y','u','i','o','p']
        row2 = ['a', 's','d','f','g','h','j','k','l']
        row3 = ['z', 'x','c','v','b','n','m']

        row_total= [row1, row2, row3]
        result = []

        for w in words:
            for r in row_total:
                if w[0].lower() in r:
                    get_r = r
                    break

            for c in w:
                j = 0
                if c.lower() not in get_r:
                    j = -1
                    break

            if j != -1:
                result.append(w)

        return result
