'''
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.

The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth.

Return the sum of each integer in nestedList multiplied by its depth.

 

Example 1:


Input: nestedList = [[1,1],2,[1,1]]
Output: 10
Explanation: Four 1's at depth 2, one 2 at depth 1. 1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10.
Example 2:


Input: nestedList = [1,[4,[6]]]
Output: 27
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3. 1*1 + 4*2 + 6*3 = 27.
Example 3:

Input: nestedList = [0]
Output: 0
 

Constraints:

1 <= nestedList.length <= 50
The values of the integers in the nested list is in the range [-100, 100].
The maximum depth of any integer is less than or equal to 50.

'''

class Solution:
    def depthSum_dfs(self, nestedList: List[NestedInteger]) -> int:
        
        def dfs(nestedList, depth):
            total = 0
            
            for nested in nestedList:
                if nested.isInteger():
                    total += nested.getInteger() * depth
                else:
                    total += dfs(nested.getList(), depth + 1)
            return total
        
        return dfs(nestedList, 1)
        
        
        '''
        Time : O(N), where N -  total number of nested elements
        On each nested list, it iterates over all of
        the nested elements directly inside that list
        (in other words, not nested further). 
        As each nested element can only be directly inside one list,
        we know that there must only be one loop iteration for each nested element. 
        This is a total of O(N) loop iterations.
        So combined, we are performing at most 2*O(N) recursive calls and loop iterations.
        We drop the 2 as it is a constant, leaving us with time complexity O(N).
        
        Space : O(N), 
        In terms of space, at most O(D) recursive calls are placed on the stack, 
        where D is the maximum level of nesting in the input. 
        For example, D=2 for the input [[1,1],2,[1,1]], 
        and D=3 for the input [1,[4,[6]]].

        In the worst case, D =N, (e.g. the list [[[[[[]]]]]])
        so the worst-case space complexity is O(N).
        
        '''

    def depthSum_bfs(self, nestedList: List[NestedInteger]) -> int:
        from collections import deque
        q = deque([(nestedList, 1)])
        depth = 1
        total = 0
        while q:
            
            nested, depth = q.popleft()

            for nest in nested:
                
                if nest.isInteger():
                    total += nest.getInteger() * depth
                else:
                    q.append((nest.getList(), depth + 1))
        
        return total
        
        
        '''
        Time : O(N), where N -  total number of nested elements
        On each nested list, it iterates over all of
        the nested elements directly inside that list
        (in other words, not nested further). 
        As each nested element can only be directly inside one list,
        we know that there must only be one loop iteration for each nested element. 
        This is a total of O(N) loop iterations.
        So combined, we are performing at most 2*O(N) recursive calls and loop iterations.
        We drop the 2 as it is a constant, leaving us with time complexity O(N).
        
        Space : O(N), 
        In terms of space, at most O(D) recursive calls are placed on the stack, 
        where D is the maximum level of nesting in the input. 
        For example, D=2 for the input [[1,1],2,[1,1]], 
        and D=3 for the input [1,[4,[6]]].

        In the worst case, D =N, (e.g. the list [[[[[[]]]]]])
        so the worst-case space complexity is O(N).
        
        '''