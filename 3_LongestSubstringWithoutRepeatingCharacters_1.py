class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :param s: str
        :return: int
        """
        Max = 0
        s1 = -1
        dict1 = {}

        for i in range(len(s)):
            if s[i] in dict1 and dict1[s[i]] > s1:
                    s1 = dict1[s[i]]
                    dict1[s[i]] = i

            else:
                dict1[s[i]] = i
                if i - s1 > Max:
                    Max = i-s1

        return Max
