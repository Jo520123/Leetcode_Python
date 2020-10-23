from collections import defaultdict
class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = defaultdict(set)

    def buildDict(self, dictionary):
        """
        :param dictionary: List[str]
        :return: None
        """
        for x in dictionary:
            for i in range(len(x)):
                idx = x[:i] + '_' + x[i+1:]
                self.table[idx].add(x[i])



    def search(self, searchWord):
        """
        :param searchWord: str
        :return:  bool
        """

        for i in range(len(searchWord)):

            idx = searchWord[:i] + '_' + searchWord[i+1:]
            SigChr = self.table[idx]

            if not SigChr:
                continue


            if len(SigChr) > 1 or searchWord[i] not in SigChr:
                print(True)
                return True

        print(False)
        return False
