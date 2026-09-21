import heapq
from collections import defaultdict
class Twitter:

    def __init__(self):
        
        #followerId -> set of followeeIds
        self.follow_map = defaultdict(set)

        #userId -> list of (count, tweetId)
        #We use a decrementing global count so Python's min-heap acts as a max-heap
        self.tweet_map = defaultdict(list)
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        #O(1) time
        #Append (decrementing_count, tweetId)
        self.tweet_map[userId].append((self.count, tweetId))
        self.count -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        #O(K + 10log K ) time, where K is the number of followers + 1
        res = []
        min_heap = []

        #Ensure the user always sees their own tweets alongside followees
        feed_users = self.follow_map[userId] | {userId}

        #Step 1: Seed heap with the MOST RECENT tweet from each user
        #Store: (count, tweetId, userId, next_idx_to_check)
        for u_id in feed_users:
            tweets = self.tweet_map[u_id]
            if tweets:
                last_idx = len(tweets) - 1
                cnt, t_id = tweets[last_idx]
                min_heap.append((cnt, t_id, u_id, last_idx - 1))

        #O(K) heapify to turn the initial K tweets into a valid heap
        heapq.heapify(min_heap)

        #Step 2: Pop at most 10 tweets globally
        while min_heap and len(res) < 10:
            cnt, t_id, u_id, next_idx = heapq.heappop(min_heap)
            res.append(t_id)

            #if this user has an older tweet, push it to the heap
            if next_idx >= 0:
                older_cnt, older_t_id = self.tweet_map[u_id][next_idx]
                heapq.heappush(min_heap, (older_cnt, older_t_id, u_id, next_idx - 1))
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        #O(1) time
        self.follow_map[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        #O(1) time 
        #discard won't crash if the key or value doesn't exist
        self.follow_map[followerId].discard(followeeId)
