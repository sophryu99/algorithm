# https://leetcode.com/problems/flood-fill/
# https://sophuu.tistory.com/67

class Solution:
    
    def check(self, r, c, rlimit, climit):
        return 0 <= r < rlimit and 0 <= c < climit
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        # locate starting number
        startnum = image[sr][sc]
        image[sr][sc] = newColor
        q = []
        visited = []
        q.append((sr, sc))
        visited.append((sr, sc))
        
        dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
        
        while q:
            qr, qc = q.pop()
            # set new direction
            for dir in range(4):
                nr = qr + dr[dir]
                nc = qc + dc[dir]
                # check for index validity
                if (nr, nc) not in visited and self.check(nr, nc, len(image), len(image[0])):
                    # if the new element is equal to startnum
                    if image[nr][nc] == startnum:
                        # append to visited and q
                        visited.append((nr, nc))
                        q.append((nr, nc))
                        # change new element to newcolor
                        image[nr][nc] = newColor
                        
        return (image)

"""
Runtime: 68 ms, faster than 95.10% of Python3 online submissions for Flood Fill.
Memory Usage: 14.1 MB, less than 98.14% of Python3 online submissions for Flood Fill.
"""
