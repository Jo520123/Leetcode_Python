class SnapshotArray:

    def __init__(self, length):
        """
        :param length: int
        """
        self.d = {}
        self.a = []

    def set(self, index, val):
        """
        :param index: int
        :param val: int
        :return:
        """
        self.d[index] = val


    def snap(self):
        """
        :return: int
        """
        self.a.append(self.d.copy())
        return len(self.a)-1


    def get(self, index, snap_id):
        """
        :param index: int
        :param snap_id: int
        :return: int
        """
        if index in self.a[snap_id]:

            return self.a[snap_id][index]
        else:
            return 0