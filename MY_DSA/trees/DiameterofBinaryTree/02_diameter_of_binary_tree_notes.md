# Problem 2: Diameter of Binary Tree — My Notes

## Pattern
Post-order Tree Aggregation — **Multi-Value Return** (extends Problem 1).
Compute one thing locally (height) while tracking a second, GLOBAL best-so-far
answer (diameter) that might not even live at the root.

---

## The ONE idea to never forget
> **`left_diameter` and `right_diameter` are answers from DISCONNECTED regions.
> You cannot add them together — they might not even touch.**
> The only thing you're allowed to add is stuff that genuinely connects
> THROUGH the current node: `left_height + right_height + 2`.

So at every node, there are exactly 3 candidates for "best diameter I know about right now":
1. `left_diameter` — best already found entirely inside left subtree
2. `right_diameter` — best already found entirely inside right subtree
3. `left_height + right_height + 2` — best path with THIS node as peak

Answer = `max` of all three. Never `+`.

---

## Mistake Log (what I actually got wrong, and the fix)

| # | What I did | Why it was wrong | Correct way to think |
|---|---|---|---|
| 1 | `current_diameter = left_diameter + right_diameter` | These are two disconnected paths that may not touch each other at all — adding them creates a path that doesn't physically exist | Only `left_height + right_height (+2)` genuinely connects through the current node. Diameters from subtrees just get compared with `max`, never added |
| 2 | Dry ran with `current_diameter = max(ld, rd, left_height+right_height)` — **missing `+2`** | `height(child)` only counts edges BELOW the child — it doesn't include the edge connecting parent → child itself | distance from node down through a child = `height(child) + 1`. So path through node = `(left_height+1) + (right_height+1) = left_height + right_height + 2` |
| 3 | Confused "height of 6" with "distance from 4 to 6" | `height(leaf)=0` describes the leaf's OWN subtree, not the edge connecting it to its parent | Always ask: "whose height is this measuring FROM?" — height is always measured from that specific node downward, not from its parent |
| 4 | Guessed naive-approach complexity as O(n^n) | Jumped to a wrong big-O without doing the actual sum first | Build the sum from small concrete numbers first `(n-1)+(n-2)+...+0`, THEN convert to Big-O. `n(n-1)/2` → **O(n²)** |
| 5 | Return type `-> int` while actually returning a list/tuple | Function signature must describe what's ACTUALLY returned | If returning 2 values, signature is `Tuple[int, int]`, and use tuple unpacking `a, b = func(x)`, not `func(x)[0]` |
| 6 | Mixed public interface and recursive helper into ONE function | Caller shouldn't have to know internals return `(height, diameter)` — they just want the diameter | Always split: public `diameter_of_binary_tree(root) -> int` calls a private `_height_and_diameter(node) -> Tuple[int,int]` helper |
| 7 | Stray `from logging import root` line | Likely autocomplete slip — unrelated import that breaks the file | Always read through imports before running; don't blindly trust autocomplete |

---

## The "+2" Derivation (write this out from memory until it's automatic)

```
distance from node -> deepest point in LEFT child's subtree  = height(left_child) + 1
distance from node -> deepest point in RIGHT child's subtree = height(right_child) + 1

path through node (peak) = (left_height + 1) + (right_height + 1)
                          = left_height + right_height + 2
```

---

## Recursive Blueprint

- **Base Case:** `node is None` -> `(height=-1, diameter=0)`
- **Recursive Hypothesis:** child call correctly returns height of its OWN subtree
  AND the best diameter found ANYWHERE inside its own subtree (not necessarily
  touching the child itself)
- **Recursive Step:**
  - `height = max(left_height, right_height) + 1`
  - `diameter = max(left_diameter, right_diameter, left_height + right_height + 2)`
- **Return Value:** `(height, diameter)` tuple
- **Decision Space:** none — compute & combine, just 2 values instead of 1

---

## Final Code
```python
from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None,
                 right: "Optional[TreeNode]" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    return _height_and_diameter(root)[1]


def _height_and_diameter(node: Optional[TreeNode]) -> Tuple[int, int]:
    if node is None:
        return -1, 0
    left_height, left_diameter = _height_and_diameter(node.left)
    right_height, right_diameter = _height_and_diameter(node.right)
    height = max(left_height, right_height) + 1
    diameter = max(left_diameter, right_diameter, left_height + right_height + 2)
    return height, diameter
```

---

## Interview Q&A I Should Be Able to Answer Cold
- Overlapping subproblems? -> No, tree = each node has ONE parent = visited once
- Naive approach (separate `height()` call inside diameter traversal) complexity? ->
  O(n^2) worst case (skewed tree) — calling a full traversal INSIDE another
  traversal multiplies complexities. General rule: fuse into ONE pass instead.
- N-ary tree version? -> pick the **top 2** child heights (not all of them,
  since a path can only enter/exit through 2 children max), formula becomes
  `top1_height + top2_height + 2`
- Weighted edges version? -> replace flat `+1` with `+edge_weight` everywhere
  height/distance is computed. Same idea reappears in Dijkstra later.
- Why tuple return over external `self.diameter` variable? -> tuple = pure
  function, no hidden side effects, easier to test/reason about. Side-effect
  version works too but hides behavior from the function signature.

---

## Takeaway for the NEXT problem
This "local compute + global best-so-far" shape is EXACTLY the same skeleton
used in **Maximum Path Sum in Binary Tree** — same trap (values can go negative
there, so an extra "should I even include this branch?" decision gets added).
Watch for how negative values change the max() logic when that comes up.
