class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        way = ['0:0']
        for i in path:
            if i == 'N':
                y += 1
                start = str(x) + ':' + str(y)
                if start in way:
                    return True
                way.append(start)
            elif i == 'E':
                x += 1
                start = str(x) + ':' + str(y)
                if start in way:
                    return True
                way.append(start)
            elif i == 'S':
                y -= 1
                start = str(x) + ':' + str(y)
                if start in way:
                    return True
                way.append(start)
            elif i == 'W':
                x -= 1
                start = str(x) + ':' + str(y)
                if start in way:
                    return True
                way.append(start)

        return False