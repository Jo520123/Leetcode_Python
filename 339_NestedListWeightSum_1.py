class Solution:
    def DepthSum(self, nested_List, cur_Level=1):
        """
               :type nestedList: List[NestedInteger]
               :rtype: int
               """
        ret = 0

        for element in nested_List:
            if element.isInteger():
                ret += cur_Level*element.getInteger()
            else:
                ret += self.DepthSum(element.getList(), cur_Level = cur_Level+1)

