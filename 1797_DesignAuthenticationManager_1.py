from collections import OrderedDict
class AuthenticationManager:

    def __init__(self, timeToLive):
        """
        :param timeToLive: int
        """
        self.timeToLive = timeToLive
        self.d = OrderedDict()

    def popexp(self, currentTime):
        while self.d and self.d.itervalues().next() <= currentTime:
            self.d.popitem(last = False)


    def generate(self, tokenId, currentTime):
        """

        :param tokenId: str
        :param currentTime: int
        :return: None
        """
        self.popexp(currentTime)
        self.d[tokenId] = currentTime + self.timeToLive


    def renew(self, tokenId, currentTime):
        """
        :param tokenId: str
        :param currentTime: int
        :return: None
        """
        self.popexp(currentTime)
        if tokenId not in self.d:
            return

        del self.d[tokenId]
        self.d[tokenId] = currentTime + self.timeToLive


    def countUnexpiredTokens(self, currentTime):
        """
        :param currentTime: int
        :return: int
        """
        self.popexp(currentTime)

        print  len(self.d)
        return len(self.d)
