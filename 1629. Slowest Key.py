class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        mx = releaseTimes[0]
        s = keysPressed[0]
        for i in range(1,len(releaseTimes)):
            if (releaseTimes[i] - releaseTimes[i-1]) > mx:
                mx = releaseTimes[i] - releaseTimes[i-1]
                s = keysPressed[i]
            elif (releaseTimes[i] - releaseTimes[i-1]) == mx:
                s = max(s, keysPressed[i])
        return s