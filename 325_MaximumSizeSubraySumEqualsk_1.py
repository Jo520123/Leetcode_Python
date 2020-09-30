class Solution():
    def maxSubArrayLen(self, nums, k):
        """
        :param nums: List[int]
        :param k: int
        :return: int
        """
        table = {}

        sum, maxl = 0, 0
        l = len(nums)

        for i in range(l):

            sum += nums[i]

            if (sum == k):
                maxl = i + 1

            elif (sum -k) in table:
                maxl = max(maxl, i - table[sum -k])

            else:
                table[sum] = i

        return maxl

x = Solution()
arry = [10,5,2,7,1,9]
k = 15
#Output : 4

print(x.maxSubArrayLen(arry, k))

arry1 = [-5, 8, -14, 2, 4, 1]
k1 = -5

print(x.maxSubArrayLen(arry1, k1))
#Output : 5