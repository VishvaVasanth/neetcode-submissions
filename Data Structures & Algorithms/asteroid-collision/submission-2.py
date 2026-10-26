
from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            alive = True

            while stack and a < 0 and stack[-1] > 0:
                if stack[-1] < abs(a):
                    stack.pop()  # Top asteroid explodes
                elif stack[-1] == abs(a):
                    stack.pop()  # Both explode
                    alive = False
                    break
                else:
                    alive = False  # Incoming asteroid explodes
                    break

            if alive:
                stack.append(a)

        return stack
