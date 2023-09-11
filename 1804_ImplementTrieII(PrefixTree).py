from collections import defaultdict
class TrieNode():
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.wTotal = 0
        self.cTotal = 0

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
            :param word: str
            :return: None
            """
        ptr = self.root

        for x in word:
            ptr = ptr.children[x]
            ptr.cTotal += 1
        ptr.wTotal += 1


    def countWordsEqualTo(self, word):
        """
                :param word: str
                :return: int
                """
        ptr = self.root

        for x in word:
            if x in ptr.children:
                ptr = ptr.children[x]
            else:

                print(0)

        print(ptr.wTotal)


    def countWordsStartingWith(self, prefix):
        """
                    :param prefix: str
                    :return: int
                    """

        ptr = self.root

        for x in prefix:
            if x in ptr.children:
                ptr = ptr.children[x]
            else:
                print(0)

        print(ptr.cTotal)


    def erase(self, word):
        """
                :param word: str
                 :return: None
                """
        ptr = self.root

        for x in word:
            if x in ptr.children:
                ptr.cTotal -= 1
                ptr = ptr.children[x]

        ptr.wTotal -= 1
