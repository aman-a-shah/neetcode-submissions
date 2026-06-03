# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        results = set()

        # recurse through tree
        def recurse_down(root):
            if not root:
                return

            if root.val == subRoot.val:
                results.add(check_same(root, subRoot))
            recurse_down(root.left)
            recurse_down(root.right)

        # when reach same root node, recursively check and add to result 
        def check_same(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1:
                return False
            elif not node2:
                return False
            
            return node1.val == node2.val and check_same(node1.left, node2.left) and check_same(node1.right, node2.right)

        recurse_down(root)
        return any(results)