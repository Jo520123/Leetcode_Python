class Solution:
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :param words1: List[str]
        :param words2: List[str]
        :param pairs: List[List[str]]
        :return: bool
        """

        if len(words1) != len(words2):
            return False

        for i, v1 in enumerate(words1):
            v2 = words2[i]

            if not (v2 == v1 or [v2, v1] in pairs or [v1, v2] in pairs):
                return False

        return True
