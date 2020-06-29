class Solution:
    def reconstructQueue(self, people):
        """
        :param people: List[List[int]]
        :return: List[List[int]]
        """
        people_d ={}
        for x in people:
            h, k = x[0], x[1]
            people_d.setdefault(h, [])
            people_d[h].append(k)

        result = []

        people = sorted(people_d.keys(), reverse = True)

        for x in people:
            people_d[x].sort()
            for y in people_d[x]:
                result.insert(y, [x,y])

        return result
