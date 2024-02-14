class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        n_pos = 1
        p_pos = 0
        for i in nums:
            if i > 0:
                ans[p_pos]= i
                p_pos+=2
            else:
                ans[n_pos] = i
                n_pos+=2
        return ans
     
        
        
        