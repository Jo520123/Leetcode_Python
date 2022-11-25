from collections import Counter
class Solution:
    def sortFeatures(self, features, responses):
        """
        :param features: List
        :param responses: List
        :return: List
        """
        
        c = Counter()

        for r in responses:
            c += Counter(set(r.split()))

        features = [[y,x] for x ,y in enumerate(features)]

        features.sort(key = lambda x : (c[x[0]], -x[1]), reverse = True)

        return [x[0] for x in features]
