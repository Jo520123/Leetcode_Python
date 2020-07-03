class Solution:
    def search(self, nums, target):
        """
        :param nums:  List[int]
        :param target: int
        :return: int
        """
        l, r = 0, len(nums)-1
        while l <=  r:
            mid = (l + r)//2
            if nums[mid] == target:
                return mid

            if target >= nums[0]:
                if nums[mid] >= nums[0] and target > nums[mid]:
                    l = mid+1
                else:
                    r = mid-1

            else:
                if nums[mid] >= nums[0] or target > nums[mid]:
                    l = mid+1
                else:
                    r = mid-1
        return -1
