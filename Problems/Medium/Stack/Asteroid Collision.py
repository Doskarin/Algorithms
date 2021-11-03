'''
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
Example 4:

Input: asteroids = [-2,-1,1,2]
Output: [-2,-1,1,2]
Explanation: The -2 and -1 are moving left, while the 1 and 2 are moving right. Asteroids moving the same direction never meet, so no asteroids will meet each other.
 

Constraints:

2 <= asteroids.length <= 10^4
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0

'''

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = [ ]
        #All we care about is whether
        #asteroid moving right will collide
        #with the one moving left
        #it means we should always append asteroids
        #moving rightwards
        for asteroid in asteroids:
            
            if asteroid > 0:
                stack.append(asteroid)
            else:
                #if there is something in stack
                #and incoming asteroid is bigger
                #than that of in stack
                #we pop it since it will destroy 
                #asteroid inside the stack
                while stack and stack[-1] > 0 and stack[-1] < -asteroid:
                    stack.pop()
                    
                #If after while loop
                #last element of stack is equal
                #to the size of asteroid
                #we pop it since both asteroids will be
                #destroyed
                if stack and stack[-1] == -asteroid:
                    stack.pop()
                    
                #if incoming asteroid's
                #size is smallest than last one's
                #we will not add it since
                #it will be destroyed
                elif stack and stack[-1] > -asteroid:
                    continue
                
                #else asteroid moving leftwards reached the rock bottom
                else:
                    stack.append(asteroid)
        return stack