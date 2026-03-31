# Last updated: 3/31/2026, 9:38:10 PM
from collections import defaultdict, deque
import heapq
class Twitter:
    def __init__(self):
        self.time = 0 
        self.user_tweets = defaultdict(deque) 
        self.following = defaultdict(set)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets[userId].appendleft((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        tweets = []
        users = self.following[userId] | {userId}
        heap = []
        for uid in users:
            for t in list(self.user_tweets[uid])[:10]:  
                heapq.heappush(heap, (-t[0], t[1]))
        news_feed = []
        for _ in range(10):
            if heap:
                news_feed.append(heapq.heappop(heap)[1])
            else:
                break
        return news_feed
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)