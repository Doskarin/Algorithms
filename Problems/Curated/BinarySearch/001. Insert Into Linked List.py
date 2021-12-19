'''
You are given a singly linked list head as well as integers pos and val. Insert a new node with value val before index pos of head.

Constraints

1 ≤ n ≤ 100,000 where n is the number of nodes in head
0 ≤ pos ≤ n
Example 1
Input

head = [1, 3, 5, 7]
pos = 2
val = 9
Output

[1, 3, 9, 5, 7]
Example 2
Input

head = [1]
pos = 0
val = 3
Output

[3, 1]
Example 3
Input

head = [2]
pos = 1
val = 5
Output

[2, 5]


'''

class LLNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Solution:

    def solve(self, head, pos, val):
        to_insert = LLNode(val)
        # Edge case №1 - When position is zero new node becomes head
        if pos == 0:
            to_insert.next = head
            return to_insert
        
        # Edge case №2 - When position is one, head's next node is the new node
        elif pos == 1:
            to_insert.next = head.next
            head.next = to_insert
            return head

        cur = head
        k = 1
        while cur.next:
            if k == pos:
                to_insert.next = cur.next
                cur.next = to_insert
                return head
            cur = cur.next
            k += 1

        # Edge case №3 - If we traversed till the end and did not insert
        # it means we reached the end and last node should our new node
        cur.next = to_insert
        return head

        '''
        Time Complexity : O(n) because we traverse the linked list linearly.

        Space Complexity : O(1) as only individual nodes are used.
        
        
        '''