class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        data = False
        nums.sort()
        
        if len(nums) < 2:
            return False
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
            
        
        
        