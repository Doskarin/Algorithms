'''
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1
 

Constraints:

1 <= intervals.length <= 104
0 <= starti < endi <= 106

'''

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        events = []
        
        for start, end in intervals:
            events.append((start, 1))
            events.append((end, -1))
            
        events.sort()
        
        max_rooms = 0
        cur_rooms = 0
        for _, room in events:
            cur_rooms += room
            max_rooms = max(max_rooms, cur_rooms)
            
        return max_rooms
            
        '''
        Time : O(NlogN), dominated by sorting
        
        Space : O(N), aux array events
        '''
            