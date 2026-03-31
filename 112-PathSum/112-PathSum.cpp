// Last updated: 3/31/2026, 9:39:56 PM
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool hasPathSum(TreeNode* root, int targetSum) {
        if (root==nullptr){
            return false;
        }
        if(root->left==nullptr && root->right==nullptr){
            return targetSum==root->val;
        }
        bool smleft = hasPathSum(root->left,targetSum-(root->val));
        bool smright = hasPathSum(root->right,targetSum-(root->val));
        return smleft || smright;
    }
};