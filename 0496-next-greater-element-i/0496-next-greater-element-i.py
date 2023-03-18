class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        for i in nums1:
            idx = nums2.index(i)
            flag = False
            for j in range(idx,len(nums2)):
                if nums2[idx] < nums2[j]:
                    flag = True
                    break
            if flag == True:
                stack.append(nums2[j])
            else:
                stack.append(-1)
        return stack
                
                
            
        
                
            
            
            
                
        