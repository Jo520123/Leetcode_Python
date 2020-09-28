class Solution():
    def groupStrings(self, strings):
        """
        :param strings: List[str]
        :return: List[List[str]]
        """
        if len(strings) == 0:
            return []

        store = dict()

        for x in strings:
            dif = ord(x[0]) - ord('a')
            shf_val = []

            for ix in x:
                if ix > x[0]:
                    shf_val.append(chr(ord(ix) - dif))
                else:
                    shf_val.append(chr(26 + ord(ix) - dif))

            shf_valstr = "".join(shf_val)

            if shf_valstr not in store:
                store[shf_valstr] = list()

            store[shf_valstr].append(x)

        return list(store.values())
