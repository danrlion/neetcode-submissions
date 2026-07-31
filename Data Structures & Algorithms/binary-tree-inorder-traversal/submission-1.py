# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer: list[int] = []
        def dfs(node):
            if node is None: # base case
                return
            left = dfs(node.left)
            if left is None:
                answer.append(node.val)
            return dfs(node.right)
        dfs(root)
        return answer