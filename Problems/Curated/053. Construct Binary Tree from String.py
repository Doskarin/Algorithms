'''
You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

 

Example 1:

       4
      / \
     2   6
    / \  /
   3  1  5


Input: s = "4(2(3)(1))(6(5))"
Output: [4,2,6,3,1,5]
Example 2:

Input: s = "4(2(3)(1))(6(5)(7))"
Output: [4,2,6,3,1,5,7]
Example 3:

Input: s = "-4(2(3)(1))(6(5)(7))"
Output: [-4,2,6,3,1,5,7]
 

Constraints:

0 <= s.length <= 3 * 10^4
s consists of digits, '(', ')', and '-' only.

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        
        
        
        def dfs(index):
            
            start = index
            while index < len(s) and (s[index] == "-" or s[index].isdigit()):
                index += 1
            
            if start == index:
                return None, index
            
            node = TreeNode(int(s[start:index]))
            
            if index < len(s) and s[index] == "(":
                index += 1
                
                node.left, index = dfs(index)
                
                index += 1
                
            if index < len(s) and s[index] == "(":
                index += 1
                
                node.right, index = dfs(index)
                
                index += 1
                
            return node, index
        
        root, _ = dfs(0)
        
        return root
    
    '''
    Time : O(N), where N represents the number of characters
    in the string representation. 
    This is because each character is processed
    exactly once and we need to process the entire string so as to form our tree.
    
    Space : O(H), where H represents the height 
    of the tree. We don't have any information
    about if the tree is balanced or not and so,
    in the worst case when the tree would be skewed left
    (can't be right according to the problem), we will have
    a recursion stack consisting of N calls and hence, 
    the overall space complexity can be O(N)
    
    '''