class Solution:
    def TwoSum(self,numbers, target):
        l, r = 0, len(numbers) -1
        while l < r:
            if numbers[l] + numbers[r] < target:
                l += 1
            if numbers[l] + numbers[r] > target:
                r -= 1
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]

