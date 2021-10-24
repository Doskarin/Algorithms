'''
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendar class:

MyCalendar() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
 

Example 1:

Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output
[null, true, false, true]

Explanation
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.
 

Constraints:

0 <= start < end <= 10^9
At most 1000 calls will be made to book.

'''

class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        
        
'''
If we maintained our events in sorted order, we could check whether an event could be booked in O(logN) time (where N is the number of events already booked) by binary searching for where the event should be placed. We would also have to insert the event in our sorted structure.
'''
class Tree:

    def __init__(self):
        self.root = None
    #TO-DO
    def insert(self, node, root = None):
        if not root:
            if not self.root:
                self.root = node
                return True
            else:
                root = self.root
        if node.start >= root.end:
            if not root.right:
                root.right = node
                return True
            return self.insert(node, root.right)
        elif node.end <= root.start:
            if not root.left:
                root.left = node
                return True
            return self.insert(node, root.left)
        else:
            return False

class MyCalendar:

    def __init__(self):
        self.tree = Tree()
        

    def book(self, start: int, end: int) -> bool:
        return self.tree.insert(Node(start, end))