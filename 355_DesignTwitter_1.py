import heapq
class Client:
    """
    Initialize structure

    """
    def __init__(self, clientId):
        self.clientId = clientId
        self.posts = set()
        self.like = set()


class Post(object):
    """
    Initialize post structure
    """
    def __init__(self, clientId, postId, count):
        self.clientId = clientId
        self.postId = postId
        self.count = count

    def __cmp__(self, other):
       return cmp(other.count, self.count)



class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.count = 0
        self.table = dict()

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
         :param userId: int
         :param tweetId:int
         :return: None
        """
        if userId not in self.table:
            self.table[userId] = Client(userId)

        post = Post(userId, tweetId, self.count)
        self.table[userId].posts.add(post)
        self.count += 1


    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
         :param userId: int
         :return: List[int]
        """
        q = []
        ans = list()

        if userId not in self.table:
            return ans

        pri_u = self.table[userId]

        for x in pri_u.posts:
            heapq.heappush(q,x)

        for y in pri_u.like:
            for z in y.posts:
                heapq.heappush(q, z)

        c = 0

        while q and c < 10:

            ans.append(heapq.heappop(q).postId)
            c += 1
        return ans


    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
         :param followerId: int
        :param followeeId: int
         :return: None
        """
        if followerId not in self.table:
            self.table[followerId] = Client(followerId)

        if followeeId not in self.table:
            self.table[followeeId] = Client(followeeId)

        if followeeId == followerId:
            return

        fan = self.table[followeeId]
        self.table[followerId].like.add(fan)


    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
          :param: int
        :param: int
         :return: None
        """
        if (followerId not in self.table) or (followeeId not in self.table) or (followerId == followeeId):
            return

        fan = self.table[followeeId]

        if fan in self.table[followerId].like:
            self.table[followerId].like.remove(fan)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
