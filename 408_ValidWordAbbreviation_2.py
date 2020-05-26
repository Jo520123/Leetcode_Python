class Solution:
    def ValidWordAbbreviation(self, word,abbr):
        """
              :type word: str
              :type abbr: str
              :rtype: bool
              """
        i, j =0,0
        while i <len(abbr):
            if j > len(word):
                return False
            if not abbr[i].isdigit():
                if abbr[i] != word[j]:
                    return False
                i +=1
                j +=1
            else:
                if abbr[i] == '0':
                    return False
                x = ''
                while i <len(abbr) and abbr[i].isdigit():
                    x += abbr[i]
                    i += 1
                j += int(x)
        return j == len(word)
