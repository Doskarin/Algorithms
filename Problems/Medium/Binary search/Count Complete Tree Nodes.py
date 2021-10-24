'''
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

 

Example 1:

         1
        / \
       2   3
      / \  /
     4  5 6
Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [1]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [0, 5 * 10^4].
0 <= Node.val <= 5 * 10^4
The tree is guaranteed to be complete.

'''

# In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible.

# That means that complete tree has 2^k nodes in the kth level if the kth level is not the last one. The last level may be not filled completely, and hence in the last level the number of nodes could vary from 1 to 2^d, where d is a tree depth.


# Now one could compute the number of nodes in all levels but the last one. 
# That reduces the problem to the simple check of how many nodes the tree has in the last level.
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        d = self.getDepth(root)
        if d == 0:
            return 1
        # Last level nodes are enumerated from 0 to 2**d - 1 (left -> right).
        # Perform binary search to check how many nodes exist.
        left, right = 1, 2**d - 1
        while left <= right:
            mid = left + (right - left) // 2
            if self.exists(mid, d, root):
                left = mid + 1
            else:
                right = mid - 1
        # The tree contains 2**d - 1 nodes on the first (d - 1) levels
        # and left nodes on the last level.
        return 2**d - 1 + left
    
    
    def exists(self, idx, depth, node):
        """
        Last level nodes are enumerated from 0 to 2**d - 1 (left -> right).
        Return True if last level node idx exists. 
        Binary search with O(d) complexity.
        """
        left, right = 0, 2**depth - 1
        for _ in range(depth):
            pivot = left + (right - left) // 2
            if idx <= pivot:
                node = node.left
                right = pivot
            else:
                node = node.right
                left = pivot + 1
        return node is not None
        
        
    def getDepth(self, node):
        d = 0
        while node.left:
            node = node.left  
            d += 1
        return d