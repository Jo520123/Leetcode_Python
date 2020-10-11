class Solution:
    def findMaxLength(self, nums):
        """
        :param nums: List[int]
        :return: int
        """

        table = dict()
        table[0] = -1
        sum = 0
        ans = 0

        for i, j in enumerate(nums):

            if j == 1:
                sum += 1

            else:
                sum -= 1

            if sum in table:
              ans = max( i-table[sum], ans)

            else:
                table[sum] = i

        return ans
