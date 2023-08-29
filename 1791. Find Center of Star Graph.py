class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        edge1, edge2 = edges[0], edges[1]
        if edge1[0] in edge2:
            return edge1[0]
        else:
            return edge1[1]