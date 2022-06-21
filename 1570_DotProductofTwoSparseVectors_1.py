from collections import defaultdict

class SparseVector:
    def __init__(self, nums):
        """
        :param nums: List[int]

        """
        self.d = defaultdict(int)

        for i,v1 in enumerate(nums):
            if v1 != 0:
                self.d[i] = v1


    def dotProduct(self, vec):
        """
        :param vec: 'SparseVector'
        :return: int
        """
        value = 0

        for i,v2 in vec.d.items():
            value += self.d.get(i,0) * v2

        return value


nums1 = [1,0,0,2,3]
nums2 = [0,3,0,4,0]
n1 = SparseVector(nums1)
n2 = SparseVector(nums2)
ans1 = n1.dotProduct(n2)

print(ans1)
#Output: 8


nums11 = [0,1,0,0,0]
nums22 = [0,0,0,0,2]
n11 = SparseVector(nums11)
n22 = SparseVector(nums22)
ans11 = n11.dotProduct(n22)

print(ans11)
#Output: 0


nums111 = [0,1,0,0,2,0,0]
nums222 = [1,0,0,0,3,0,4]
n111 = SparseVector(nums111)
n222 = SparseVector(nums222)
ans111 = n111.dotProduct(n222)

print(ans111)
#Output: 6
