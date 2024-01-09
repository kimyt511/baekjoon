# 872 Leaf-Similar Trees
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        stack1 = []

        def search1(node):
            if node == None:
                return
            if (node.left == None) & (node.right == None):
                stack1.append(node.val)
            search1(node.left)
            search1(node.right)

        search1(root1)
        stack2 = []

        def search2(node):
            if node == None:
                return
            if (node.left == None) & (node.right == None):
                stack2.append(node.val)
            search2(node.left)
            search2(node.right)

        search2(root2)
        return stack1 == stack2
