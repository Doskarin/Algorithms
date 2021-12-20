'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        n = len(lists)
        
        interval = 1
        
        while interval < n:
            
            for i in range(0, n - interval, 2 * interval):
                lists[i] = self.mergeLists(lists[i], lists[i + interval])
            interval *= 2
            
        return lists[0] if n > 0 else None
    
    
    def mergeLists(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy
        
        while l1 and l2:
            
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
                
            elif l1.val > l2.val:
                tail.next = l2
                l2 = l2.next
            
            tail = tail.next
            
        if l1:
            tail.next = l1
            
        if l2:
            tail.next = l2
            
        return dummy.next
    
    '''
    Time : O(n*k*logk), where n -  average size of lists, k - number of lists
    
    Space : O(1), no extra space is used
    
    
    
    '''