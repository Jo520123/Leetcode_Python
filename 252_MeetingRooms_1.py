class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def CanAttendMeeting(self, interval):
        """
                :type interval: List[Interval]
                :rtype: bool
                """
        interval.sort(key = lambda x: x.start)

        for i in range(1,len(interval)):
            if interval[i].start < interval[i-1].end:
                return False
        return True


