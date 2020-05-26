class Soution:
    def CanConstruct(self, ransomeNote, magazine):
        """
                :type ransomNote: str
                :type magazine: str
                :rtype: bool
                """
        if len(ransomeNote) > len(magazine):
            return False

        letter =[0] * 26
        for c in magazine:
            letter[ord(c) - 97] += 1
        for c in ransomeNote:
            letter[ord(c) -97] -= 1
            if letter[ord(c) -97] < 0:
                return False
        return True

