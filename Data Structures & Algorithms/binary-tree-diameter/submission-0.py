# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.maxD = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def getDepth(root):
            if not root:
                return 0
            
            left = 1 + getDepth(root.left)
            right = 1 + getDepth(root.right)

            self.maxD = max(self.maxD, left-1 + right-1)

            return max(right, left)

        getDepth(root)

        return self.maxD
        