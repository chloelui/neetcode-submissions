# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        level = 0

        q = deque([root])

        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr:
                    if len(res) <= level:
                        res.append([])
                    res[level].append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
            level += 1

        return res