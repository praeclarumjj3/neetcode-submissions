from typing import List
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = {}   # userId -> list of (time, tweetId)
        self.follows = {}  # userId -> set of followeeIds

    def _add_user(self, userId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
            self.follows[userId] = set()

    def postTweet(self, userId: int, tweetId: int) -> None:
        self._add_user(userId)
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self._add_user(userId)

        heap = []

        users = set(self.follows[userId])
        users.add(userId)

        for uid in users:
            if self.tweets[uid]:
                idx = len(self.tweets[uid]) - 1
                time, tweetId = self.tweets[uid][idx]
                heapq.heappush(heap, (-time, tweetId, uid, idx))

        feed = []

        while heap and len(feed) < 10:
            neg_time, tweetId, uid, idx = heapq.heappop(heap)
            feed.append(tweetId)

            if idx > 0:
                idx -= 1
                time, tweetId = self.tweets[uid][idx]
                heapq.heappush(heap, (-time, tweetId, uid, idx))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self._add_user(followerId)
        self._add_user(followeeId)

        if followerId != followeeId:
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self._add_user(followerId)
        self._add_user(followeeId)

        self.follows[followerId].discard(followeeId)