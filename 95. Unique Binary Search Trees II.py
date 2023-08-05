# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n <= 0:
            return []


        def tree(left, right):
            if left > right:
                return [None]
            result = []
            for i in range(left, right + 1):
                for l in tree(left, i - 1):
                    for r in tree(i + 1, right):
                        node = TreeNode(i)
                        node.left = l
                        node.right = r
                        result.append(node)
            return result if result else [None]

        return tree(1, n)