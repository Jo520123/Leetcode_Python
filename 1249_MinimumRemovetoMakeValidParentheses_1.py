class Solution:
    def minRemoveToMakeValid(self, s):
        """
        :param s: str
        :return: str
        """
        Del=[]
        stack=[]
        sb = []

        for i in range(len(s)):
            if(s[i] == '('):
                stack.append(i)
            elif(s[i] == ')'):
                if not stack:
                    Del.append(i)
                else:
                    stack.pop()

        while(stack):
            Del.append(stack.pop())

        for i in range(len(s)):
            if i not in Del:
                sb.append(s[i])

        return ''.join(sb)

