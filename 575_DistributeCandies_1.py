class Solution:
    def distributeCandies(self, candies):
        """
        :param candies: List[int]
        :return: int
        """
        dif = len(set(candies))
        half = len(candies)//2

        ans = min(half, dif)

        return ans
