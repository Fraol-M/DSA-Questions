# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        

        cnt = 0
        def dfs(node):
            nonlocal cnt
            if not  node:
                return 0



            left = dfs(node.left)
            right = dfs(node.right)


            value = max(left, right)
            cnt = max(left + right, cnt)
            # print("node", node.val, "---", value, "cnt", "-", cnt)
            

            return value + 1



        dfs(root)

        return cnt
