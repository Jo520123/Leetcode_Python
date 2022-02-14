class UndergroundSystem:

    def __init__(self):
        self.entry = {}
        self.exit = {}



    def checkIn(self, id, stationName, t):
        """
        :param id: int
        :param stationName: str
        :param t: int
        :return: None
        """
        if stationName not in self.entry:
            self.entry[stationName] = [[id,t]]

        else:
            self.entry[stationName].append([id, t])



    def checkOut(self, id, stationName, t):
        """
        :param id: int
        :param stationName: str
        :param t: int
        :return: None
        """
        if stationName not in self.exit:
            self.exit[stationName] = [[id, t]]

        else:
            self.exit[stationName].append([id, t])


    def getAverageTime(self, startStation, endStation):
        """
        :param startStation: str
        :param endStation: str
        :return:float
        """
        ans = []

        for x in self.entry[startStation]:
            for y in self.exit[endStation]:
                if x[0] == y[0]:

                    ans.append(abs(y[1] - x[1]))


        return float(sum(ans) / len(ans))
