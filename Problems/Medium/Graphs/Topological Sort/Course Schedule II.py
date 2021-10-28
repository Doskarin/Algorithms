'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.

'''
#Recursive approach using three coloring method
NOT_VISITED = 0
IN_PROGRESS = 1
DONE = 2

def dfs(v, edges, states, top_sorted_values):
    states[v] = IN_PROGRESS
    
    for u in edges[v]:
        if states[u] == IN_PROGRESS:
            return False
        if states[u] == NOT_VISITED:
            if not dfs(u, edges, states, top_sorted_values):
                return False
    top_sorted_values.append(v)
    states[v] = DONE
    return True

class Solution:
    def findOrder(self, n: int, p: List[List[int]]) -> List[int]:
        edges = [[] for i in range(n)]
        
        for [a, b] in p:
            edges[b].append(a)
            
        top_sorted_values = []
        states = [NOT_VISITED] * n
        
        for v in range(n):
            if states[v] == NOT_VISITED:
                
                if not dfs(v, edges, states, top_sorted_values):
                    return []
                
        return list(reversed(top_sorted_values))

#Kahn's Topological Sort algorithm    
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        valid_order = [ ]
        indegrees = [0] * numCourses
        graph = defaultdict(list)
        
        #Build graph and indegrees array
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegrees[course] += 1
            
        q = deque()
        #Build up initial queue with courses
        #that have indegree of 0 - these courses
        #do not have any prerequisites
        for course, indegree in enumerate(indegrees):
            if indegree == 0:
                q.append(course)
                
        
                
        while q:
            cur_course = q.popleft()
            #Popped course does not have
            #any prerequisites - append it to the result
            valid_order.append(cur_course)
            
            for child in graph[cur_course]:
                #Decrease indegrees of all courses
                #that had this prerequisite
                #If indegree after that operation will be zero
                #it means it is a next candidate 
                indegrees[child] -= 1
                if indegrees[child] == 0:
                    q.append(child)
        return valid_order if len(valid_order) == numCourses else []