# 1026 Maximum Difference Between Node and Ancestor
# dfs로 해당 subtree의 최대값, 최소값, 최대차이값을 return
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def get_val(node, ans):
            if node == None:
                return (-1, 100000, 0)
            left = get_val(node.left, ans)
            right = get_val(node.right, ans)
            max_val = max(left[0], right[0])
            min_val = min(left[1], right[1])
            ans = max(left[2], right[2])
            if max_val != -1:
                ans = max(ans, abs(max_val - node.val))
            if min_val != 100000:
                ans = max(ans, abs(min_val - node.val))
            return (max(max_val, node.val), min(min_val, node.val), ans)

        return get_val(root, 0)[2]
