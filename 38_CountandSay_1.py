class Solution:
    def CountandSay(n):

        if (n==1):
            return "1"
        if (n==2):
            return "11"

        h = "11"
        for i in range(3,n+1):
            h += '$'
            l = len(h)
            c = 1
            tmp = ""

            for j in range(1,l):

                if (h[j] != h[j-1]):
                    tmp += str(c+0)
                    tmp += h[j-1]
                    c = 1

                else:
                    c +=1
            h = tmp
        return h

