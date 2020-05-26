class Solution:
    def ContainsNearbyDuplicate(self, nums, m):
        look_up = {}
        for i, num in enumerate(nums):
            if num not in look_up:
                look_up[num] = i
            else:
                if i - look_up[num] <= m:
                    return True
                look_up[num] = i
        return False
