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
    int goodNodes = 0;

    public void dfs(TreeNode root, int pathMax) {
        if (root == null) {
            return;
        }

        pathMax = Math.max(pathMax, root.val);
        if (pathMax == root.val) {
            goodNodes++;
        }

        dfs(root.left, pathMax);
        dfs(root.right, pathMax);
    }
    public int goodNodes(TreeNode root) {
        int pathMax = root.val;

        dfs(root, pathMax);
        return goodNodes;
        
    }
}
