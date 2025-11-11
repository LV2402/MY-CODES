# 2️⃣ clever way (binary search)

# instead of counting one by one, we guess in the middle.

# imagine you’re thinking:
# “hmm the square root of 11 must be between 1 and 11… let me check the middle (6).”

# 6×6=36 → too big! so it must be smaller than 6.

# now range is 1…5. check middle (3).

# 3×3=9 → fits! maybe bigger?

# check 4. 4×4=16 → too big.

# so answer = 3.

# this is like playing “guess the number” but with squares.

def floor_sqrt_binary(n):
    lo, hi = 0, n
    ans = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid * mid <= n:
            ans = mid    # works, try higher
            lo = mid + 1
        else:
            hi = mid - 1 # too big, go lower
    return ans
