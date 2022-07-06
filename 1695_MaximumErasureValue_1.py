class Solution:
    def maximumUniqueSubarray(self, nums):
        """
        :param nums: List[int]
        :return: int
        """
        d = {}
        lp, rp = 0, 0
        total = 0
        accumulate = [0]
        ans = 0

        for x in nums:
            total += x
            accumulate.append(total)

        while rp < len(nums):

            if nums[rp] not in d:
                d[nums[rp]] = True
                ans = max(accumulate[rp+1] - accumulate[lp], ans)
                rp += 1

            else:
                while lp < rp and nums[rp] in d:
                    d.pop(nums[lp])
                    lp += 1

        return ans