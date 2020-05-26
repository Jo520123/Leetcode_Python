class Solution:
    def PlusOne(self, d):
        """
        :param d: List[int]
        :return: List{int}
        """
        for i in range(1,len(d)+1):
            if(d[-i]==9): 
                d[-i] = 0
            else:     
                d[-i]+=1
                break
        if(d[0]==0):
            d[0]=1
            d.append(0)
        return d
