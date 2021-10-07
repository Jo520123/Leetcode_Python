import bisect
class Solution:
    def isPossibleDivide(self, nums, k):
        """
        :param nums: List[int]
        :param k: int
        :return: bool
        """
        nums = sorted(nums)

        while len(nums) > 0:
            first = nums.pop(0)
            next = first + 1
            rem = k - 1

            while rem > 0:
                id = bisect.bisect_left(nums, next)

                if id >= 0 and id < len(nums) and nums[id] == next:
                    rem -= 1
                    next += 1
                    del nums[id]
                    continue

                return False


        return rem == 0
