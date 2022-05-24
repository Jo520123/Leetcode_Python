import bisect

class Solution:
    def avoidFlood(self, rains):
        """
        :param rains: List[int]
        :return: List[int]
        """

        l = len(rains)
        result = []
        dry = []
        full  = {}


        for i in range(l):

            if rains[i] == 0:
                dry.append(i)
                result.append(1)


            else:
                if rains[i] in full:

                    if len(dry) == 0:

                        result = []

                        break

                    else:

                        preday = full[rains[i]]

                        dryidx = bisect.bisect_right(dry, preday)

                        if dryidx >= len(dry):

                            result = []

                            break

                        else:

                            result[dry[dryidx]] = rains[i]

                            dry.pop(dryidx)


                full[rains[i]] = i

                result.append(-1)


        return result
