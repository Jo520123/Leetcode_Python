class Solution:
    def threeSum(self, nums):
        """
        :type nums:  List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        result = []

        for i in range(0,n-2):
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break

            if nums[i] + nums[n-1]+ nums[n-2] < 0:
                continue

            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i+1, n-1
            while  left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left+1 < right and nums[left] == nums[left+1]:
                        left+=1
                    left+=1
                    while left < right-1 and nums[right] == nums[right-1]:
                        right -=1
                    right-=1
                elif total < 0:
                    left+=1
                else:
                    right -=1

        return result


nums = [-1, 0, 1, 2, -1, -4]
x = Solution()
print(x.threeSum(nums))