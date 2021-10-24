'''
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

 

Example 1:

            10
           /  \
          5   -3
         / \    \
        3   2    11
       / \   \
      3  -2   1
        
        
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown. 5 -> 3, 5 -> 2 -> 1, -3 -> 11


Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
 

Constraints:

The number of nodes in the tree is in the range [0, 1000].
-10^9 <= Node.val <= 10^9
-1000 <= targetSum <= 1000


'''

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        #Global variable which we will be incrementing as we explore the tree
        self.numberOfPaths = 0
        
        #Method to calculate sum path for a given node
        def test(node, curSum):
            if not node:
                return
            if curSum == node.val:
                self.numberOfPaths += 1    
            left = test(node.left, curSum - node.val)
            right = test(node.right, curSum - node.val)
        
        #On each node we launch test method from the start
        #to explore new possibilities
        def dfs(node):
            if not node:
                return 
            test(node, targetSum)
            left = dfs(node.left)
            right = dfs(node.right)
            
            
        dfs(root)
        return self.numberOfPaths