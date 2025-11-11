# 4️⃣ fancy math trick (log + exp)

# there’s a formula:

# 𝑛=𝑒0.5⋅ln⁡(𝑛)n	​

# =e0.5⋅ln(n)

# that’s like using a calculator’s magic powers. works the same, just mathy.

import math

def floor_sqrt_exp_log(n):
    guess = int(math.exp(0.5 * math.log(n)))
    if (guess + 1) * (guess + 1) <= n:
        guess += 1
    return guess
