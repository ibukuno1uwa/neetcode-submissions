# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxDepth_ = 0

        if not root:
            return maxDepth_

        stack = [(root, 1)]
        maxDepth_ = 1
        seen = set()
        
        while stack:
            parent, depth  = stack[-1]

            if parent.left and parent not in seen:
                stack.append((parent.left, depth + 1))

                maxDepth_ = max(maxDepth_, depth + 1)
                seen.add(parent)
            
            else:
                parent, depth = stack.pop()
                if parent.right:
                    stack.append((parent.right, depth + 1))
                    maxDepth_ = max(maxDepth_, depth + 1)
        
        return maxDepth_
