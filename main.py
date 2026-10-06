class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 374. Guess Number Higher or Lower
    # Might not work in leetcode and stuff since 
    # the problem does not define guess in code
    def guess(self, n: int) -> int:
        pick = 0
        return -1 if n > pick else 1

    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            res = self.guess(mid)
            if res == 0:
                return mid
            elif res < 0:
                right = mid - 1
            else:
                left = mid + 1
        return -1
    # 104. Maximum Depth of Binary Tree
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
