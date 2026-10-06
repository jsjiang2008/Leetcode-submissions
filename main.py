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
    # 872. Leaf Similar Trees
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        a = self.findLeaves(root1)
        b = self.findLeaves(root2)
        return True if a == b else False


    def findLeaves(self, root: TreeNode | None) -> str:
        if root is None:
            return ""
        if root.left is None and root.right is None:
            return " " + str(root.val)
        return self.findLeaves(root.left) + self.findLeaves(root.right)