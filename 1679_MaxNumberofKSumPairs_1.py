class Solution:
    def maxOperations(self, nums, k):
        """
        :param nums: List[int]
        :param k: int
        :return: int
        """

        d = {}
        count = 0

        for x in nums:
            if x in d and (2 * x) != k:
                d[x] += 1

            else:
                if k- x in d:
                    if d[k-x] == 1:
                        del d[k-x]

                    else:
                        d[k-x] -= 1

                    count += 1

                else:
                    d[x] = 1


        return count
