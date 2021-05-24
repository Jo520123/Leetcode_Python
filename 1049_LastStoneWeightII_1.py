import heapq
class Solution:
    def lastStoneWeightII(self, stones):
        """
        :param stones: List[int]
        :return: int
        """
        rev = list(map(lambda x :-x, stones))
        heapq.heapify(rev)

        while len(rev) > 1:
            first = heapq.heappop(rev)

            if rev:
                second = heapq.heappop(rev)

                if first != second:
                    heapq.heappush(rev, -abs(first-second))


        if not rev:
            return 0
        else:
            return -rev[0]



x = Solution()
stones = [2,7,4,1,8,1]
##Output: 1
print(x.lastStoneWeightII(stones))

stones1 = [31,26,33,21,40]
##Output: 5
print(x.lastStoneWeightII(stones1))



print("1111111111111111111111111111")
numbers = (1, 2, 3, 4)

result = map(lambda x: -x, numbers)
print(result)
heapq.heapify(result)
print(result)
print(type(result))
print(list(result))

x = heapq.heappop(result)
print(x)
print(result)
x = heapq.heappop(result)
print(x)
print(result)
print("1111111111111111111111111111")

# initializing list 1
li1 = [5, 7, 9, 4, 3]

# initializing list 2
li2 = [5, 7, 9, 4, 3]

# using heapify() to convert list into heap
heapq.heapify(li1)
heapq.heapify(li2)
print (li1)
print (li2)

# using heappushpop() to push and pop items simultaneously
# pops 2

print (heapq.heappushpop(li1, 2))

# using heapreplace() to push and pop items simultaneously
# pops 3

print (heapq.heapreplace(li2, 2))


print("2222222222222222222222222222222222222")

# initializing list
li = [5, 7, 9, 1, 3]
print (type(li))
print (li)
# using heapify to convert list into heap
heapq.heapify(li)
print (type(li))
print (li)


# printing created heap
#print ("The created heap is : ", end = "")
#print (list(li))

stones = [2,7,4,1,8,1]
#Output: 1

stones1 = [31,26,33,21,40]
#Output: 5

stones2 = [1,2]
#Output: 1

