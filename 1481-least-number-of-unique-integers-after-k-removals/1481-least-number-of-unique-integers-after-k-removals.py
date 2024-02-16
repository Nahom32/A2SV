class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq_holder = Counter(arr)
        rm = 0
        values = list(freq_holder.values())
        heapq.heapify(values)
        while values != []:
            rm += heapq.heappop(values)
            if rm > k:
                return len(values) + 1
        return 0
        
        
        
        
        
        
        