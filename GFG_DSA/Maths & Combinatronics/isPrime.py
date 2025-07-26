import math # We need this for the square root calculation later

def isPrime(n):
    # Rule 1: Check if n is 1 or 0 (or negative)
    # Our first check: Is the number even eligible to be in the club?
    if n <= 1:
        return False # No, numbers <= 1 are never prime. Case closed for these.

    # Rule 2: Special cases for 2 and 3
    # These are the smallest prime numbers, and our later general checks
    # might miss them or treat them incorrectly if we don't handle them first.
    if n == 2 or n == 3:
        return True # Yes, 2 and 3 are definitely prime. We found our answer quickly!

    # Rule 3: Quick check for divisibility by 2 or 3
    # Our "first sweep" for obvious non-primes.
    # If a number is divisible by 2 (and it's not 2 itself) or by 3 (and it's not 3 itself),
    # it immediately has an extra divisor and can't be prime.
    if n % 2 == 0 or n % 3 == 0:
        return False # This number has extra divisors (2 or 3), so it's not prime.

    # Rule 4: The main investigation (checking other potential divisors)
    # This is the smartest part of our detective work.
    i = 5
    # Why math.sqrt(n)?
    # Imagine n = 100. If 10 divides 100 (10*10), then 10 is the square root.
    # If 2 divides 100 (2*50), then 50 is *another* divisor. But 2 is *before* the square root.
    # If 20 divides 100 (20*5), then 20 is *after* the square root, but 5 is *before*.
    # The key idea: If a number `n` has *any* divisor `D` greater than its square root,
    # then `n` MUST also have another divisor `d` that is *smaller* than its square root.
    # So, we only need to search for divisors up to `math.sqrt(n)`. If we don't find any,
    # then there won't be any larger ones either! It saves a lot of checking.
    while i <= math.sqrt(n):
        # Why i and i+2? And why i += 6?
        # This is the "smart skip" strategy.
        # We've already checked for divisibility by 2 and 3.
        # All other prime numbers (after 3) can *always* be written in one of two forms:
        # (6 * some_number - 1) OR (6 * some_number + 1)
        # Examples:
        # 5 = (6*1 - 1)
        # 7 = (6*1 + 1)
        # 11 = (6*2 - 1)
        # 13 = (6*2 + 1)
        # 17 = (6*3 - 1)
        # 19 = (6*3 + 1)
        # So, instead of checking every single odd number (5, 7, 9, 11, 13, 15, 17, ...),
        # we only need to check numbers that fit these patterns.
        #
        # `i` starts at 5.
        # `n % i == 0` checks if `n` is divisible by `i` (which is $6k-1$ form).
        # `n % (i + 2) == 0` checks if `n` is divisible by `i + 2` (which is $6k+1$ form).
        #
        # `i += 6` means we jump from 5 to 11 (5+6), then from 11 to 17 (11+6), etc.
        # This way, we efficiently check numbers of the form $6k-1$ and $6k+1$.
        if n % i == 0 or n % (i + 2) == 0:
            return False # We found an extra divisor, so it's not prime!
        i += 6 # Move to the next pair of potential prime factors

    # Rule 5: If we reached here, no extra divisors were found!
    # Congratulations! Our investigation found no evidence of extra divisors.
    return True # This number is prime!

# How to use our detective agency:
n = 7 # Let's investigate the number 7
if(isPrime(n)): # Call our detective function
  print("true") # If it returns True, print "true"
else:
  print("false") # If it returns False, print "false"