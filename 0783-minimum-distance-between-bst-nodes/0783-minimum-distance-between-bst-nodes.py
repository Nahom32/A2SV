# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        lin = []
        def bfs(root):
            if not root:
                return 
            else:
                bfs(root.left)
                lin.append(root.val)
                bfs(root.right)
        bfs(root)
        m = float('inf')
        for i in range(1,len(lin)):
            if m > lin[i] -lin[i-1]:
                m = lin[i] - lin[i-1]
        print(lin)
        return m
        