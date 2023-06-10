class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        l = []
        for i in asteroids:
            while l and i < 0 < l[-1]:
                if l[-1] < -i:
                    l.pop()
                    continue
                elif l[-1] == -i:
                    l.pop()
                break
            else:
                l.append(i)
        return l