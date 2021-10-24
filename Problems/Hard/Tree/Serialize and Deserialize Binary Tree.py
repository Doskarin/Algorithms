'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

Example 1:

           1
          / \
         2   3
            / \
           4   5
         


Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]


'''
class Codec:
    #Method to serialize the tree
    def serialize(self, root):
        def dfs(node):
            #If node is not None we append string value to the result and traverse left and right subtrees
            if node:
                res.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
            else:
                #Each time we encounter leaves we append "Null"
                res.append('Null')
        res = [ ]
        dfs(root)
        return ','.join(res)
    #Method to deserialize the tree from string to TreeNode  
    def deserialize(self, data):
        
        def dfs():
            #Each time we traverse take next item from iterator
            val = next(it)
            #If it returns 'Null' it means we reached leaves, hence return None
            if val == 'Null':
                return None
            #Create new TreeNode
            node = TreeNode(int(val))
            #Its left child is whatever we return from dfs'ing to the left
            node.left = dfs()
            #Its right child is whatever we return from dfs'ing to the right
            node.right = dfs()
            return node
        
        #Initialize iterator to get all values
        it = iter(data.split(','))
        return dfs()