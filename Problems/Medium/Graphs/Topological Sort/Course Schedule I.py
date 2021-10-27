'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 10^5
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.

'''
#Recursive approach with three coloring

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        visited = [0] * numCourses
        #We have three state :
        #0 - node was never reached
        #1 - node is processed
        #2 - node is being processed
        #if we happen to process node that is already being
        #processed - it means we have cycle and can return False
        def dfs(node):
            if visited[node] == 2:
                return False
            
            if visited[node] == 1:
                return True
            
            visited[node] = 2
            for child in graph[node]:
                if not dfs(child):
                    return False
               
            visited[node] = 1
            
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
            
        return True
    
#Kahn's algorithm for Topological Sorting
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        inDegree = [0] * numCourses
        #Keep track of indegrees
        #and start with all courses that have indegree of 0
        #as we go through the deque keep adding those courses
        #whose indegree become zero
        #at the end, if it is possible to make toposort
        #every course's indegree will be equal to 0
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            inDegree[course] += 1
        
        q = deque()
        for course, indegree in enumerate(inDegree):
            if indegree == 0:
                q.append(course)
        
        while q:
            course = q.popleft()
            for child in graph[course]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    q.append(child)
                    
        return not any(inDegree)