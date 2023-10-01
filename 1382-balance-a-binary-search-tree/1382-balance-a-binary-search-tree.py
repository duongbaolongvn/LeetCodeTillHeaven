# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        node = []

        def in_order_traverse(root):
            if root:
                in_order_traverse(root.left)
                node.append(root)
                in_order_traverse(root.right)

        def building_balance_tree(left, right):
            if left > right: return
            mid = (right + left)//2
            root = node[mid]
            root.left = building_balance_tree(left, mid - 1)
            root.right = building_balance_tree(mid + 1,right)
            return root

        in_order_traverse(root)
        return building_balance_tree(0, len(node)-1)