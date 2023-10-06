class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        holder = set()
        for i in range(k):
            if i >= len(nums):
                return False
            if nums[i] in holder:
                return True
            else:
                holder.add(nums[i])
        for i in range(k,len(nums)):
            if nums[i] in holder:
                return True
            else:
                holder.remove(nums[i-k])
                holder.add(nums[i])
        return False
        
        
        
        