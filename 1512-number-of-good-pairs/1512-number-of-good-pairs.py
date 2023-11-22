class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hsh = Counter()
        for i in nums:
            hsh[i]+=1
        idx = 0
        for i in hsh:
            if hsh[i] != 1:
                idx+=((hsh[i]*(hsh[i]-1)))//2
        return idx
            
            
            
            
        