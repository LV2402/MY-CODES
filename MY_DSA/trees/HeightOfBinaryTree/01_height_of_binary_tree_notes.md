# Problem 1: Height of Binary Tree — My Notes

## Pattern
Post-order Tree Aggregation — "ask children first, combine at parent."
Every future tree problem (Diameter, Balanced Check, Max Path Sum, LCA) reuses this shape.

---

## The ONE idea to never forget
> **A leaf is NOT special. `None` is special.**

I initially wanted to write `if leaf: return -1` — special-casing leaves.
That breaks the moment a node has ONE child instead of zero, because I never defined
what `height(None)` returns for that missing side.

**Fix:** only `node is None` is a base case. Leaves just naturally fall out of the
formula because both their children are `None`.

👉 **Rule for all future tree recursion:** never special-case a "type" of node
(leaf, single-child, etc). Only special-case the **absence of a node** (`None`).
Let the formula handle every real node uniformly.

---

## Mistake Log (what I actually got wrong, and the fix)

| # | What I did | Why it was wrong | Correct way to think |
|---|---|---|---|
| 1 | Leaf returns `-1` directly (Design A) | No answer defined for `height(None)` when a node has only 1 child | Only `None` is base case; leaf uses the same formula as everyone else |
| 2 | Said "height of node returns height of the tree" | Circular — didn't say what unit (edges vs nodes) | Height = **number of edges** on longest root→leaf path. Base case `-1` exists so a single node correctly computes to `0` |
| 3 | Mixed up `height(3)`'s return value with the final answer `height(1)` | Easy to conflate "value of a sub-call" with "final root answer" once tree >2 levels deep | Track each call's return value separately; only the **root call** is the "final answer" |
| 4 | Said space complexity = "O(1) and O(n)" without separating them | Auxiliary space and call-stack space are DIFFERENT things | Auxiliary space: O(1). Call stack: O(h) — O(log n) balanced, O(n) skewed |
| 5 | Said n=10^5 skewed tree → "TLE" | O(n) is fast enough for 10^5 — the real issue isn't speed | It's a **RecursionError** (Python's default recursion depth ~1000), not a time-limit issue |
| 6 | `node==None` | Works but not idiomatic / linter warns | `None` is a singleton → always use `is None`, not `== None` |
| 7 | Wrote `Optional[TreeNode]-> int` | Put return type INSIDE the param type hint | Return type goes after `)`: `def f(node: Optional[TreeNode]) -> int:` |

---

## Recursive Blueprint (fill this template for every future tree problem)

- **Base Case:** `node is None` → return `-1` (edge convention)
- **Recursive Hypothesis:** trust `height(node.left)` gives correct height of the
  subtree rooted there — don't mentally trace inside it
- **Recursive Step:** `max(left_height, right_height) + 1`
- **Return Value:** edges on longest path from `node` to a leaf
- **Decision Space:** none — pure compute & combine (no choices = easier than backtracking)

---

## Final Code
```python
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None,
                 right: "Optional[TreeNode]" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def height_of_binary_tree(node: Optional[TreeNode]) -> int:
    if node is None:
        return -1
    left_height = height_of_binary_tree(node.left)
    right_height = height_of_binary_tree(node.right)
    return max(left_height, right_height) + 1
```

---

## Interview Q&A I Should Be Able to Answer Cold
- Why -1 as base case, not 0? → derived from edge-counting convention, not arbitrary
- Overlapping subproblems here? → No (tree = each node visited once, no shared subproblems)
- n = 10^5, skewed tree — what breaks? → RecursionError, not TLE
- Two fixes without changing algorithm logic? → `sys.setrecursionlimit()` (risky/band-aid)
  OR convert to iterative using an explicit stack
- Why DFS over BFS here? → doesn't matter much for height, but BFS is natural when you
  want "level by level" info directly, no combine-step needed
- What assumption does this make? → input is a valid tree (no cycles, one parent per node).
  Graphs need a `visited` set — trees don't, because acyclic-ness is guaranteed by definition

---

## Takeaway for the NEXT problem (Diameter of Binary Tree)
Diameter reuses this exact height logic, but I'll need to return/track **two things**
at once (height AND diameter-so-far) instead of just one value. This is my first
exposure to "multi-value recursion" — watch for how I handle it.
