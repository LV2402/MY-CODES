# 1️⃣ silly but easy way (counting)

# just start from 1 and keep trying squares until you go past n.
# like:

# n=11

# try 1×1=1 (ok)

# try 2×2=4 (ok)

# try 3×3=9 (ok)

# try 4×4=16 (too big!)
# stop. answer = 3

def floor_sqrt_loop(n):
    x = 1
    while x * x <= n:   # keep going as long as square fits
        x += 1
    return x - 1        # last good number