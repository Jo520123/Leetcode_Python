class Solution:
    def letterCombinations(self, digits):
        """
        :param digits: str
        :return: List[str]
        """
        if len(digits) == 0:
            return []

        digit_table = {
            0: "0",
            1: "1",
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }

        result = [""]

        for x in digits:
            list = []
            for y in digit_table[int(x)]:
                for z in result:
                    list.append(z+y)
            result = list
        return result
