# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        current = root
        prev = None

        while current:
            if current.left is None:
                result.append(current.val)
                current = current.right
            else:
                prev = current.left
                while prev.right:
                    prev = prev.right
                prev.right = current
                temp = current
                current = current.left
                temp.left = None

        return result