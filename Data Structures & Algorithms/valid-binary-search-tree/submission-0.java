/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    boolean isValid = true;
    long prev = Long.MIN_VALUE;

    public void dfs(TreeNode root) {
        if (root == null) {
            return;
        }
        dfs(root.left);

        if (!(prev < root.val)) {
            isValid = false;
        }
        prev = root.val;
        dfs(root.right);
    }
    public boolean isValidBST(TreeNode root) {

        dfs(root);
        return isValid;
        
    }
}
