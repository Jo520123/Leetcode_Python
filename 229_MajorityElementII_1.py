class Solution:
    def majorityElement(self, nums):
        """
        :param nums: List[int]
        :return:   List[int]
        """
        n1, n2 = 0,0
        c1, c2 = 0,0
        result = []

        for i in nums:
            if i == n1:
                c1+=1
            elif i == n2:
                c2+=1
            elif c1 == 0:
                n1 = i
                c1 = 1
            elif c2 ==0:
                n2 = i
                c2 = 1
            else:
                c1-=1
                c2-=1

        c1,c2 = 0,0
        for i in nums:
            if i == n1:
                c1+=1
            elif i == n2:
                c2+=1

        if c1 > len(nums)//3:
            result.append(n1)

        if c2 > len(nums) // 3:
            result.append(n2)

        return result













