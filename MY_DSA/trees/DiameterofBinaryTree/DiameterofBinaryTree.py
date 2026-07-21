from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None,
                 right: "Optional[TreeNode]" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    # public function: calls the helper, returns ONLY the diameter (an int)
    return _height_and_diameter(root)[1]


def _height_and_diameter(node: Optional[TreeNode]) -> Tuple[int, int]:
    # private helper: does the actual recursion, returns (height, diameter)
    if node is None:
        return -1, 0
    left_height, left_diameter = _height_and_diameter(node.left)
    right_height, right_diameter = _height_and_diameter(node.right)
    height = max(left_height, right_height) + 1
    diameter = max(left_diameter, right_diameter, left_height + right_height + 2)
    return height, diameter