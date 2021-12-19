'''
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.

 

Example 1:


Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]

Explanation
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False
 

Constraints:

The number of nodes in the tree is in the range [1, 105].
0 <= Node.val <= 106
At most 105 calls will be made to hasNext, and next.
 

Follow up:

Could you implement next() and hasNext() to run in average O(1) time and use O(h) memory, where h is the height of the tree?

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        
        self.leftmost_inorder(root)
        
        
    def leftmost_inorder(self, node):
        
        while node:
            self.stack.append(node)
            node = node.left
        

    def next(self) -> int:
        left_most = self.stack.pop()
        if left_most.right:
            self.leftmost_inorder(left_most.right)
        return left_most.val
        

    def hasNext(self) -> bool:
        return len(self.stack) > 0
        
    '''
    Time : next - O(N) worst case, O(1) amortized TC
    hasNext is the easier of the lot since all
    we do in this is to return true if there are any
    elements left in the stack. Otherwise, we return false.
    So clearly, this is an O(1) operation every time.
    Let's look at the more complicated function now to see
    if we satisfy all the requirements in the problem statement
    
    next involves two major operations.
    One is where we pop an element from the stack which
    becomes the next smallest element to return. 
    This is a O(1) operation. However, we then make a call
    to our helper function _inorder_left which iterates 
    over a bunch of nodes. This is clearly a linear time 
    operation i.e. O(N) in the worst case. This is true.
    
    However, the important thing to note 
    here is that we only make such a call 
    for nodes which have a right child. 
    Otherwise, we simply return. Also, even 
    if we end up calling the helper function, 
    it won't always process N nodes. They will
    be much lesser. Only if we have a skewed 
    tree would there be N nodes for the root.
    But that is the only node for which we 
    would call the helper function.
    
    Thus, the amortized (average) time
    complexity for this function would 
    still be O(1) which is what the question 
    asks for. We don't need to have a solution
    which gives constant time operations for every call.
    We need that complexity on average and that is what we get.
    
    
    Space : O(N)
    
    
    
    '''