class Solution:
    def GetSum(self,aa,bb):
        """
               :type aa: int
               :type bb: int
               :rtype: int
               """

        MAX = 0x7FFFFFFF
        mask = 0xFFFFFFFF
        while bb != 0:
            aa, bb = (aa^bb) & mask, ((aa&bb) <<1) & mask
        return aa if aa <= MAX else ~(aa ^ mask)

