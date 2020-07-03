class Solution:
    def merge(self, intervals):
        """
        :param intervals: List[List[int]]
        :return: List[List[int]]
        """

        result = []
        intervals.sort(key=lambda x: x[0])

        l = len(intervals)
        i = 0
        while i < l:
            cs = intervals[i][0]
            ce = intervals[i][1]
            if result:
                ps,pe = result[-1]
                b = min(ce,pe)
                s = max(cs,ps)

                if s <= b:
                    if ce > pe:
                        result[-1][1] = ce
                else:
                    result.append(intervals[i])
            else:
                result.append(intervals[i])

            i += 1

        return result
