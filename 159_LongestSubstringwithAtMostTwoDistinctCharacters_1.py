class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :param s: str
        :return: int
        """
        left, max_len = 0, 0
        store = {}

        for i, j in enumerate(s):
            if j in store:
                store[j] += 1

            else:
                store[j] = 1

            while len(store) > 2:

                store[s[left]] -= 1

                if  store[s[left]] == 0:
                    del store[s[left]]

                left += 1

            max_len = max(max_len, i-left+1)

        return max_len
