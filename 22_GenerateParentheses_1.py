class Solution:
    def generateParenthesis(self, n):
        if n == 0:
            return []

        result = []
        self.valid(n, n, '', result)
        return result

    def valid(self, left, right, item, result):
        if right < left:
            return
        if  left == 0 and right == 0:
            result.append(item)
        if left > 0:
            self.valid(left-1, right, item + '(', result)
        if right > 0:
                self.valid(left, right-1, item + ')', result)