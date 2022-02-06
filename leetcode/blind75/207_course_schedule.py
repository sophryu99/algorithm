# https://leetcode.com/problems/course-schedule/

# Check if a cycle exists in a directed graph
"""
prerequisites[i] = [ai, bi] 
must take course bi first if you want to take course ai.

prereqs = [[1,0], [3, 2], [2, 1]]
graph = [[], [], [], []]
visited = [0, 0, 0, 0]

graph = [[], [0], [1], [2]]
dfs(graph, visited, 0)

visited = [-1, 0, 0, 0]
...
dfs(graph, visited, 3)
visited = [0, 0, 0, -1]
for j in graph[3]:
    dfs(graph, visited, 2)
    
    visited = [0, 0, -1, -1]

"""
class Solution:
    def canFinish(self, numCourses, prerequisites):
        # Initialize a graph structure
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        
        # Store the values in the graph
        for pair in prerequisites:
            graph[pair[0]].append(pair[1])
        
        # Perform dfs per each node(courses)
        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return False
        return True
    
    def dfs(self, graph, visited, i):
        # If ith course is already visited, a cycle exists, return False
        if visited[i] == -1:
            return False
        
        # If reached the end, return True
        if visited[i] == 1:
            return True
        
        # Mark as visited
        visited[i] = -1
        
        # For every nodes, visit all the neighbors
        for j in graph[i]:
            # If a node is already visited, return False
            if not self.dfs(graph, visited, j):
                return False
            
        # After visiting all the neighbors, mark as visited
        visited[i] = 1
        return True

"""
Runtime: 92 ms, faster than 93.99% of Python3 online submissions for Course Schedule.
Memory Usage: 16.4 MB, less than 59.01% of Python3 online submissions for Course Schedule.
"""