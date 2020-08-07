class Solution:
    def fourSum(self, nums, target):
        """
        :param nums: List[int]
        :param target: int
        :return: List[List[int]]
        """
        result = []
        d = {}
        nums = sorted(nums)

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                if sum not in d.keys():
                    d[sum] = [(i,j)]
                else:
                    d[sum].append((i,j))


        for i in range(len(nums)):
            for j in range(i+1, len(nums)-2):
                ans = target - nums[i]- nums[j]
                if ans in d.keys():
                    for m,n in d[ans]:
                        if m > j:
                            result.append((nums[i], nums[j], nums[m], nums[n]))
        new_result = []
        for x in set(result):
            fi_res = list(x)
            new_result.append(fi_res)

        return new_result
