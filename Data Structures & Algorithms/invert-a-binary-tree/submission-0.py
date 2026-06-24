# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 
        right_child = root.right
        left_child  = root.left

        root.left = right_child
        root.right = left_child

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        