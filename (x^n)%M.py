def powMod(x, n, M):
    res = 1 # 'res' (result) will store our final answer. It starts at 1 because anything to the power of 0 is 1.

    # This loop continues as long as the exponent 'n' is 1 or more.
    # We are breaking down the exponent 'n' bit by bit.
    while n >= 1:

        # --- Case 1: If 'n' (the exponent) is ODD ---
        # An odd exponent means there's a 'single' x that needs to be multiplied into our result.
        # Think of x^5 as x * x^4. We take out that single 'x' (and include it in 'res'),
        # and then deal with the remaining even exponent (x^4).
        if n % 2 == 1:
            # We multiply our current 'res' by 'x' and immediately take the modulo M.
            # This is crucial: (A * B) % M = ((A % M) * (B % M)) % M.
            # By taking modulo at each step, we prevent numbers from becoming too large.
            res = (res * x) % M

            # Since we've accounted for one 'x' (by multiplying it into 'res'),
            # we decrease the exponent 'n' by 1 to make it even.
            n -= 1
        # --- End Case 1 ---

        # --- Case 2: If 'n' (the exponent) is EVEN ---
        # When the exponent is even, we can use the property: x^(2k) = (x^k)^2.
        # This allows us to halve the exponent and square the base.
        # For example, x^8 = (x^4)^2 = ((x^2)^2)^2. This makes it much faster!
        else:
            # Square the base 'x' and take the modulo M.
            # This effectively prepares 'x' for the halved exponent.
            x = (x * x) % M

            # Halve the exponent 'n'.
            # 'n //= 2' is integer division (e.g., 4 // 2 = 2, 5 // 2 = 2).
            n //= 2
        # --- End Case 2 ---

    # Once the loop finishes (n becomes 0), 'res' holds the final result.
    return res

# --- Example Execution: x=3, n=2, M=4 ---
if __name__ == "__main__":
    x, n, M = 3, 2, 4
    print(powMod(x, n, M))