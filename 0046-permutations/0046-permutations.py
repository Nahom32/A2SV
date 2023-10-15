class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        pr = []
        idx = set()
        def backtrack(pth:list):
            if len(pth) == len(nums):
                pr.append(pth)
            else:
                for i in range(len(nums)):
                    if i not in idx:
                        idx.add(i)
                        backtrack(pth+[nums[i]])
                        idx.remove(i)
        backtrack([])
        return pr
                    
                
                
        