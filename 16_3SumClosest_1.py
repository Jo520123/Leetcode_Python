class Solution:
    def threeSumClosest(self, nums, target):
        """
        :param nums:  List[int]
        :param target: int
        :return: int
        """
        nums_sort = sorted(nums)
        result = nums_sort[0] + nums_sort[1] + nums_sort[len(nums)-1]

        for i in range(len(nums)-2):
            if i>0 and nums_sort[i] == nums_sort[i-1]:
                continue
            left = i +1
            right = len(nums)-1
            while left < right:
                value = nums_sort[i] + nums_sort[left] + nums_sort[right]
                if abs(value-target) < abs(result-target):
                    result = value
                if value == target:
                    return target
                elif value < target:
                    left += 1
                else:
                    right -= 1
        return result

