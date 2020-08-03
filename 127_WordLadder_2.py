from collections import deque
class Solution:
    def ladderLength(self, beginWord , endWord, wordList):
        """
        :param beginWord: str
        :param endWord: str
        :param wordList: List[str]
        :return: int
        """
        w_list = set(wordList)
        if endWord not in w_list:
            return 0

        BFS = deque()
        BFS.append((1, beginWord))

        while BFS:
            l, w = BFS.popleft()
            if w == endWord:
                return l

            for i in range(len(w)):
                for x in [chr(ord('a')+i) for i in range(26)]:
                    nw = w[:i] + x + w[i+1:]
                    if nw in w_list and nw != w:
                        w_list.remove(nw)
                        BFS.append((l+1, nw))
        return 0
