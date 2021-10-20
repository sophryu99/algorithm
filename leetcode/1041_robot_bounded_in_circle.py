# https://leetcode.com/problems/robot-bounded-in-circle/

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # Directions for North, West, South, East
        directions = [[0, 1], [-1, 0], [0, -1], [1, 0]]
        
        # Direction index
        diridx = 0
        
        # Initial direction: North
        face = directions[diridx] 
        
        # Initial start point
        x, y = 0, 0
        
        instructions = list(instructions)
        
        for ins in instructions:
            if ins == 'G':
                x += face[0]
                y += face[1]
            # Direction needs to circulate
            elif ins == 'L':
                diridx += 1
                if diridx > 3:
                    diridx = 0
                face = directions[diridx]
            elif ins == 'R':
                diridx -= 1
                if diridx < 0:
                    diridx = 3
                face = directions[diridx]
            
        if x == 0 and y == 0 or diridx != 0:
            return True
        return False
    
    
"""
Start time: 2:5 - 2:40 (35 min)

Runtime: 54 ms, faster than 12.08% of Python3 online submissions for Robot Bounded In Circle.
Memory Usage: 14.3 MB, less than 17.16% of Python3 online submissions for Robot Bounded In Circle.
"""