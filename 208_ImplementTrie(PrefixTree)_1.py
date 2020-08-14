from collections import defaultdict

class TreeNode:
    def __init__(self):
        self.child_node = defaultdict(TreeNode)
        self.w = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        present = self.root
        for x in word:
            present = present.child_node[x]
        present.w = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        present = self.root

        for x in word:
            present = present.child_node.get(x)
            if present is None:
                return False
        return present.w
        #return True


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        present = self.root
        for x in prefix:
            present = present.child_node.get(x)
            if present is None:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
"""
trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
"""

x = Trie()
x.insert("apple")
q = x.search("apple")
print(q)
qqq = x.search("app")
print(qqq)
qq = x.startsWith("app")
print(qq)
qqq = x.startsWith("123")
print(qqq)

"""
k = "apple"

def deful():
    return 3

c = defaultdict(deful)

for x in k:
    print(x)
    cc = c[x]

print(cc)
"""
