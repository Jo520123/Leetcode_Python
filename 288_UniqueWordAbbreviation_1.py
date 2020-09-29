from collections import defaultdict
class ValidWordAbbr():
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :param  dictionary: List[str]
        """
        self.table = defaultdict(set)
        for x in dictionary:
            abr = self.abbreviation(x)
            self.table[abr].add(x)

    def isUnique(self, word):
        """
        check if a word is unique.
        :param  word: str
         :return: bool
        """
        abr = self.abbreviation(word)
        if self.table[abr] < {word} or self.table[abr] == {word}:
            print("True")
            return True
        else:
            print("False")
            return False


    def abbreviation(self, word):
        if len(word) <= 2:
            return word

        return word[0] + str( len(word) -2 )+ word[-1]
