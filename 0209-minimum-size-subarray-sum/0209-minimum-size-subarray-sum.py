class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        s =0
        ans = float("inf")
        i=0
        while i < len(nums):
            s +=nums[i]
            while(s >= target):
                ans = min(ans, i+1-l)
                s-=nums[l]
                l+=1
            i+=1
        if ans != float("inf"):
            return ans
        else:
            return 0
        
        
        