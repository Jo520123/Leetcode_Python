class Solution:
    def maxDistance(self, arrays):
        """
        :param arrays: List[List[int]]
        :return: int
        """
        l = len(arrays)
        start_v = arrays[0][0]
        end_v = arrays[0][len(arrays[0])-1]
        ans = 0

        for i in range(1, l):
            m_v = arrays[i][0]
            M_v = arrays[i][len(arrays[i])-1]
            ans = max(abs(M_v-start_v),abs(m_v-end_v),ans)
            start_v = min(m_v, start_v)
            end_v = max(M_v, end_v)


        return ans
