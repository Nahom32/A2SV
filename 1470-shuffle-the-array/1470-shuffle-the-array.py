class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffled_array = []
        i = 0 
        j = n
        while j < len(nums):
            shuffled_array.append(nums[i])
            shuffled_array.append(nums[j])
            i+=1
            j+=1
        return shuffled_array
            
            
            
            
        