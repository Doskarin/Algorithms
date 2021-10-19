'''
A storekeeper is a game in which the player pushes boxes around in a warehouse trying to get them to target locations.

The game is represented by an m x n grid of characters grid where each element is a wall, floor, or box.

Your task is to move the box 'B' to the target position 'T' under the following rules:

The character 'S' represents the player. The player can move up, down, left, right in grid if it is a floor (empty cell).
The character '.' represents the floor which means a free cell to walk.
The character '#' represents the wall which means an obstacle (impossible to walk there).
There is only one box 'B' and one target cell 'T' in the grid.
The box can be moved to an adjacent free cell by standing next to the box and then moving in the direction of the box. This is a push.
The player cannot walk through the box.
Return the minimum number of pushes to move the box to the target. If there is no way to reach the target, return -1.

Input: grid = [["#","#","#","#","#","#"],
               ["#","T","#","#","#","#"],
               ["#",".",".","B",".","#"],
               ["#",".","#","#",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: 3
Explanation: We return only the number of times the box is pushed.

Example 2:

Input: grid = [["#","#","#","#","#","#"],
               ["#","T","#","#","#","#"],
               ["#",".",".","B",".","#"],
               ["#","#","#","#",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: -1

Example 3:

Input: grid = [["#","#","#","#","#","#"],
               ["#","T",".",".","#","#"],
               ["#",".","#","B",".","#"],
               ["#",".",".",".",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: 5
Explanation:  push the box down, left, left, up and up.

'''


class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        #Find coordinates of Box, Person and Target
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'B':
                    start_box = (r, c)
                if grid[r][c] == 'S':
                    start_person = (r, c)
                if grid[r][c] == 'T':
                    target = (r, c)
        
        #Method to calculate Manhattan distance between box and target, later to be used for pushing into the heap
        def distance(box):
            return abs(box[0] - target[0]) + abs(box[1] - target[1])
        
        #Method to check if current location is out of bounds
        def out_of_bounds(location):
            r, c = location
            if r < 0 or r >= rows:
                return True
            if c < 0 or c >= cols:
                return True
            return grid[r][c] == '#'
        
        #Initialize heap with distance to target, number of moves we made so far, coordinates of the person and the box
        heap = [[distance(start_box), 0, start_person, start_box]]
        
        #Visited set to keep track of the states we have already been in, the state - (coordinates of person, coordinates of box) 
        visited = set()
        while heap:
            #Pop closest candidate to the target
            _, moves, person, box = heapq.heappop(heap)
            
            #If box's coordinates are equal to target's - return number moves it took to reach it
            if box == target:
                return moves
            
            #If we have already been in this state - continue, no need to explore further
            if (person, box) in visited:
                continue
            
            #Add state to the visited set
            visited.add((person, box))
            if out_of_bounds(person):
                continue
                
            #Start exploring 4 directions
            for direction in directions:
                #Calculate person's coordinates
                new_person = (person[0] + direction[0], person[1] + direction[1])
                
                #Check if person is inbounds
                if out_of_bounds(new_person):
                    continue
                #If person's new coordinates happened to be at box's coordinates it means we can start moving box in certain direction
                if new_person == box:
                    new_box = (box[0] + direction[0], box[1] + direction[1])
                    
                    #Check if box is inbounds
                    if out_of_bounds(new_box):
                        continue
                    
                    #If we found box we push it to the heap with new moves + moves we made so far also keeping in mind that box will have new coordinates
                    heapq.heappush(heap, [distance(new_box) + moves + 1, moves + 1, new_person, new_box])
                else:
                    #Otherwise box will not move but person will
                    heapq.heappush(heap, [distance(box) + moves, moves, new_person, box])
        return -1
    
    
    
    
    
    
    
    
    
    
    
    
    