# https://leetcode.com/problems/asteroid-collision/

"""
Collsion condition
- If left is positive and right is negative
"""
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        left = 0
        right = 1
        
        while right < len(asteroids):
            # Check if right ele is negative
            if asteroids[right] < 0 and asteroids[left] > 0:
                # If they are the same weight
                if abs(asteroids[left]) == abs(asteroids[right]):
                    asteroids.pop(right)
                    asteroids.pop(left)
                    if left > 0:
                        left -=1
                        right -= 1
                
                # If right asteroid is larger in weight
                elif abs(asteroids[left]) < abs(asteroids[right]):
                    asteroids.pop(left)
                    if left > 0:
                        left -= 1
                        right -=1
                else:
                    asteroids.pop(right)
            
            # If right ele is positive, increment right
            else:
                left += 1
                right += 1
            
        return asteroids

"""
Runtime: 144 ms, faster than 26.31% of Python3 online submissions for Asteroid Collision.
Memory Usage: 15.3 MB, less than 87.31% of Python3 online submissions for Asteroid Collision."""
