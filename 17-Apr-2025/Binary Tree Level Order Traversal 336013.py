# Problem: Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        queue = deque([[root, 0]])
        depth = 0
        dic = defaultdict(list)

        while queue:
            node, depth = queue.popleft()

            if node:
                dic[depth].append(node.val)
                depth+=1

                if node.left:
                    queue.append([node.left, depth])
                
                if node.right:
                    queue.append([node.right, depth])

        ans = []
        for key, val in dic.items():
            ans.append(val)
        
        return ans

        
