from collections import defaultdict

class Logger:
    time_len = 10

    def __init__(self):

        self.timeToMessages = defaultdict(set)

    def ShouldPrintMessage(self, time_stamp, message):
        """
        :type time_stamp: int
        :type message: str
        :rtype: bool
        """
        old_Times = list( self.timeToMessages.keys() )

        for oldTime in old_Times:
            if time_stamp - oldTime >= self.time_len:
                del self.timeToMessages[ oldTime ]

        for oldTime in self.timeToMessages:
            if message in self.timeToMessages[oldTime]:
                return False

        self.timeToMessages[ time_stamp ].add( message )
        return True
