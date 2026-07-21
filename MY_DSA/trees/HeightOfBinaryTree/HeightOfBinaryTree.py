from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None,
                 right: "Optional[TreeNode]" = None) -> None:
        self.val = val
        self.left = left
        self.right = right
        
def height_of_binary_tree(node: Optional[TreeNode])-> int:
    if node is None:
        return -1
    left_height = height_of_binary_tree(node.left)
    right_height = height_of_binary_tree(node.right)
    return max(left_height, right_height) + 1