# https://leetcode.com/problems/find-if-path-exists-in-graph/

from collections import deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        # Initialize a graph structure
        graph = {}
        
        for edge in edges:
            graph[edge[0]] = graph.get(edge[0], []) + [edge[1]]
            graph[edge[1]] = graph.get(edge[1], []) + [edge[0]]

        # Create a deque and set
        q = deque()
        visited = set()
        
        # Add the starting vertex to the q and track as visited
        q.append(start)
        visited.add(start)
        
        while q:
            # Get the first vertex from the q
            node = q.popleft()
            # If the end vertex has reached, return True
            if node == end:
                return True
            
            # Get every adjacent nodes of the current node
            for adjacent_node in graph[node]:
                # If the adjancent node has not been visited
                if adjacent_node not in visited:
                    # Append to q and track as visited
                    q.append(adjacent_node)
                    visited.add(adjacent_node)
        
        return False
        
        
"""
Runtime: 4176 ms, faster than 5.01% of Python3 online submissions for Find if Path Exists in Graph.
Memory Usage: 107.4 MB, less than 42.42% of Python3 online submissions for Find if Path Exists in Graph.
"""
