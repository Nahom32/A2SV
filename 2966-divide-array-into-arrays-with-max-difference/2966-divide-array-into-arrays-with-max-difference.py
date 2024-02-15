class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        retval = []
        i = 0
        while i <= len(nums)-3:
            if nums[i+2]-nums[i] > k:
                return []
            retval.append([nums[i],nums[i+1],nums[i+2]])
            i+=3
        return retval
            
            
        