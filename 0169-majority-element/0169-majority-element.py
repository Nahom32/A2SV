class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        le = len(nums)//2
        data = Counter()
        for i in nums:
            data[i]+=1
            if data[i] > le:
                return i
            
      
        
        
        
        
        
        