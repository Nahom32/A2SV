class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        pr = []
        track = set()
        def backtrack(paths):
            if len(nums) == len(paths) and paths not in pr:
                pr.append(paths)
            else:
                for i in range(len(nums)):
                    if i not in track:
                        track.add(i)
                        backtrack(paths + [nums[i]])
                        track.remove(i)
        backtrack([])
        return pr