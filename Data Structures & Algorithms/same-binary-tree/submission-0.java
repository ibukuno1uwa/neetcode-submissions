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
    private boolean same = true;
    private void dfs(TreeNode root1, TreeNode root2) {
            if (root1 == null || root2 == null) {
                if (root1 == null && root2 == null) {
                    return;
                }
                same = false;
                return;
            }

            if (root1.val != root2.val) {
                same = false;
                return;
            }

            dfs(root1.left, root2.left);
            dfs(root1.right, root2.right);

        }

    public boolean isSameTree(TreeNode p, TreeNode q) {

        dfs(p, q);
        return same;


        
    }
}
