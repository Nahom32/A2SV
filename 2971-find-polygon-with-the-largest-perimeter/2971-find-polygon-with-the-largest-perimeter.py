class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if len(nums) < 3: return -1
        nums.sort()
        tot = -1
        prefix = [0]
        for i in nums:
            prefix.append(prefix[-1] + i)
        prefix.pop(0)
        for i in range(2,len(prefix)):
            if ((prefix[i]-prefix[i-1]) < prefix[i-1]):
                tot = prefix[i]
        return tot
        
        
        
        