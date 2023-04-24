class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            y = heapq.heappop(stones)
            if len(stones) >= 1:
                x = heapq.heappop(stones)
                if y != x:
                    heapq.heappush(stones,y-x)
        if len(stones) != 0:
            print(stones)
            return -1*heapq.heappop(stones)
        else:
            return 0
            
        