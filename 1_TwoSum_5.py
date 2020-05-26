nums= [2,7,11,15]
target= 17

def TwoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
"""
    d = {}
    for i, num in enumerate(nums):
                m = target - num
                if m not in d:
                    d[num] = i
                else:
                    return [d[m], i]


print(TwoSum(nums, target))