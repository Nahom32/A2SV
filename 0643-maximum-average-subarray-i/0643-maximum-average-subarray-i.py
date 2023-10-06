class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        mx=tot= sum(nums[:k])/k
        for i in range(k,len(nums)):
            tot-=nums[i-k]/k
            tot+=nums[i]/k
            if tot > mx:
                mx = tot
        return mx
            
        