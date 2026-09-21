import heapq
from collections import defaultdict
class Twitter:

    def __init__(self):
        #probably have a dict for each user like their followers, like a dict of {user: set(followers)}
        #have a queue of most recent like tweets? like (user: tweet)
        #or do we want to have another dic for each user like their tweets like
        #{user: [tweets]}
        #have like an artificial time started at 0, and increment by 1 for each time someone tweets?

        #userId -> set of followeeIds
        self.follow_network = defaultdict(set)

        #userId -> list of [time, tweetId]
        self.tweets = defaultdict(list)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        #O(1) time

        self.tweets[userId].append([self.time, tweetId])
        
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        
        min_heap = []

        #A user sees their own tweets + tweets of people they follow
        #Using | creates a combined set without mutating self.follow_network
        feed_users = self.follow_network[userId] | {userId}

        for user in feed_users:
            for time, tweet in self.tweets[user]:
                if len(min_heap) < 10:
                    heapq.heappush(min_heap, (time, tweet))
                elif time > min_heap[0][0]:
                    heapq.heappushpop(min_heap, (time, tweet))

        #We have the 10 most recent in min_heap, but min_heap[0] is the oldest of the 10.
        #Pop from heap or sort by descending to return the most recent first.
        res = []
        while min_heap:
            res.append(heapq.heappop(min_heap)[1])

        #reverse so newest(highest timestamp) is at index 0
        return res[::-1]

        

    def follow(self, followerId: int, followeeId: int) -> None:

        self.follow_network[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        #O(1) time 
        self.follow_network[followerId].discard(followeeId)
