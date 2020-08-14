from collections import defaultdict
class TreeNode:
    def __init__(self):
        self.child_node = defaultdict(TreeNode)
        self.w = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        present = self.root

        for x in word:
            present.child_node[x] = present
        present.w = True

    def same(self, word, r, i):
        if r is None:
            return False

        if i == len(word):
            return r.w

        if word[i] != '.':
            return self.same(word, r.child_node.get(word[i]), i + 1)

        else:
            for x in r.child_node.values():
                if self.same(word, x, i + 1):
                    return True

            return False

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.same(word, self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
