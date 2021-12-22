'''
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

 

Example 1:

         1
        / \
       2   3

Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:

         4
        / \
       9   0
      / \
     5   1 
Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 9
The depth of the tree will not exceed 10.



'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def sumNumbers_dfs(self, root: TreeNode) -> int:
        
            self.total = 0
            
            def dfs(node, cur_sum):
                if node:
                    if not node.left and not node.right:
                        self.total += (10*cur_sum + node.val)
                        return
                    else:
                        dfs(node.left, 10*cur_sum + node.val)
                        dfs(node.right, 10*cur_sum + node.val)
            dfs(root, 0)
            
            return self.total
        
        

        '''
        Time : O(N), we visit each node at least once
        
        Space : O(H), to keep the recursion stack,where H - tree height
        
        '''
    def sumNumbers_stack(self, root: TreeNode) -> int:
        
        stack = [(root, 0)]
        
        total = 0
        
        while stack:
            
            node, cur_sum = stack.pop()
            
            if node:
                
                if not node.left and not node.right:
                    cur_sum = 10 * cur_sum + node.val
                    total += cur_sum
                    
                if node.left:
                    stack.append((node.left, 10*cur_sum + node.val))
                    
                if node.right:
                    stack.append((node.right, 10*cur_sum + node.val))
                    
        return total

        '''
        Time : O(N), we visit each node at least once
        
        Space : O(H), we keep the stack of node which at worst can reach
        up to H in size, where H is a tree height



        '''

        