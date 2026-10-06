import numpy as np
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

    # 437. Path Sum III
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        prefixSum = {0: 1}
        def dfs(node, currentSum):
            if node is None:
                return 0
            currentSum += node.val

            ans = prefixSum.get(currentSum - targetSum, 0)

            prefixSum[currentSum] = prefixSum.get(currentSum, 0) + 1

            ans += dfs(node.left, currentSum)
            ans += dfs(node.right, currentSum)

            prefixSum[currentSum]  -= 1

            return ans
        return dfs(root, 0)
    
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

    # 1448. Count Good Nodes in Binary Tree
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxSeen):
            if node is None:
                return 0
            ans = 1 if node.val >= maxSeen else 0
            maxSeen = max(maxSeen, node.val)
            return ans + dfs(node.left, maxSeen) + dfs(node.right, maxSeen)
            
        return dfs(root, root.val)

    