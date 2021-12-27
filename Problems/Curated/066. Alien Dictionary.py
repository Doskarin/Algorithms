'''
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s comes before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.

 

Example 1:

Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
Example 2:

Input: words = ["z","x"]
Output: "zx"
Example 3:

Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of only lowercase English letters.

'''
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        from collections import deque, defaultdict
        graph = defaultdict(set)
        indegree = {c : 0 for word in words for c in word}
        
        for first, second in zip(words, words[1:]):
            for u, v in zip(first, second):
                if u != v:
                    if v not in graph[u]:
                        graph[u].add(v)
                        indegree[v] += 1
                    break
            else:
                if len(first) > len(second):
                    return ""
                
        
        q = deque([c for c in indegree if indegree[c] == 0])
        
        output = []
        
        while q:
            cur = q.popleft()
            output.append(cur)
            for child in graph[cur]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    q.append(child)
        
        if len(output) != len(indegree):
            return ""
        
        return "".join(output)
        '''
        Time : O(C), where C -  total length of all the words in the input list, added together
        There were three parts to the algorithm;
        identifying all the relations, putting them into an adjacency list, and then converting it into a valid alphabet ordering.

        In the worst case, the first and
        second parts
        require checking every letter of every
        word (if the difference between two words was always in the last letter). This is O(C).

        For the third part, recall that a breadth-first search
        has a cost of O(V+E), where VV is the number of vertices 
        and EE is the number of edges. Our algorithm has the same 
        cost as BFS, as it too is visiting each edge and node once
        (a node is visited once all of its edges are visited,
        unlike the traditional BFS where it is visited once one edge is visited).
        Therefore, determining the cost of our algorithm requires determining how many nodes and edges there are in the graph.

        Nodes: We know that there is one vertex for each unique letter, i.e. O(U) vertices.

        Edges: Each edge in the graph was generated 
        from comparing two adjacent words in the input list.
        There are N - 1N−1 pairs of adjacent words, and only
        one edge can be generated from each pair. This might initially 
        seem a bit surprising, so let's quickly look at an example. We'll use English words.

        abacus
        algorithm
        The only conclusion we can draw is that b is before l.
        This is the reason abacus appears before algorithm in an English dictionary.
        The characters afterward are irrelevant. It is the same for the "alien"
        alphabets we're working with here. The only rule we can draw is the one
        based on the first difference between the two words.

        Also, remember that we are only generating rules for adjacent words. 
        We are not adding the "implied" rules to the adjacency list. For example,
        assume we have the following word list.

        rgh
        xcd
        tny
        bcd
        We are only generating the following 3 edges.

        r -> x
        x -> t
        t -> b
        We are not generating these implied rules (the graph structure shows them indirectly).

        r -> t
        r -> b
        x -> b
        So with this, we know that there are at most N - 1 edges.
        
        
        Space : O(1) or O(U + min(U^2, N)), where U - be the total number
        of unique letters in the alien alphabet. 
        While this is limited to 26 in the question description, 
        we'll still look at how it would impact the complexity 
        if it was not limited (as this could potentially be a follow-up question).
        N - the total number of strings in the input list.
        
        The adjacency list uses the most auxiliary memory.
        This list uses O(V+E) memory, where VV is the number
        of unique letters, and EE is the number of relations.

        The number of vertices is simply UU; the number of unique letters.

        The number of edges in the worst case is min(U^2, N),
        as explained in the time complexity analysis.

        So in total the adjacency list takes O(U + O(U+min(U^2,N)) space.

        So for the question we're given, where U is a constant
        fixed at a maximum of 26, the space complexity is simply O(1). This is because UU is fixed at 26, and the number of relations is fixed at 26^2, so O(min(26^2, N)) = O(26^2) = O(1)

        But when we consider an arbitrarily large number of possible
        letters, we use the size of the adjacency list; O(U + min(U^2, N))
        
        
        '''