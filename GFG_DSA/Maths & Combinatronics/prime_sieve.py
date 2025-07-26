import math # We import the 'math' module to use math.sqrt() later for optimization.

def sieve(n):
    """
    This function implements the Sieve of Eratosthenes algorithm
    to find all prime numbers up to a given number 'n'.

    A prime number is a whole number greater than 1 that has no
    positive divisors other than 1 and itself (e.g., 2, 3, 5, 7, 11).

    Args:
        n (int): The upper limit, meaning we want to find all prime
                 numbers from 2 up to and including 'n'.

    Returns:
        list: A list containing all prime numbers found up to 'n'.
    """

    # Step 1: Create a boolean list to track the prime status of numbers.
    # Imagine a long row of light switches, one for each number from 0 to 'n'.
    # Initially, we assume ALL numbers are prime (light is ON, represented by True).
    # We create a list of 'True' values of size (n + 1) because list indices
    # start from 0, and we need an index for 'n' itself.
    # For example, if n=10, the list will have 11 elements (indices 0 to 10).
    prime = [True] * (n + 1)

    # We know that 0 and 1 are NOT prime numbers by definition.
    # While the algorithm will naturally ignore them later, explicitly
    # marking them False can sometimes be done, but in this specific
    # implementation, they are simply ignored because our loops start from 2.
    # prime[0] = False # Optional: Mark 0 as not prime
    # prime[1] = False # Optional: Mark 1 as not prime

    # 'p' is our current "prime candidate" or "filter number".
    # We start with the first known prime number, which is 2.
    p = 2

    # Step 2: The Core Sieve Algorithm (The "Crossing Out" Phase).
    # We iterate through potential prime numbers ('p') and mark their multiples as non-prime.
    # The loop continues as long as p*p is less than or equal to 'n'.
    # Why p*p? Because if a number 'X' has a factor greater than its square root,
    # it must also have a factor smaller than its square root. So, we only need
    # to check for prime factors up to math.sqrt(n).
    # Checking up to p*p <= n is the same as checking up to p <= math.sqrt(n).
    while (p * p) <= n:

        # Check if the current number 'p' is still marked as True (i.e., it's considered prime so far).
        # If prime[p] is False, it means 'p' is a composite number (e.g., 4, 6)
        # and its multiples would have already been marked False by a smaller prime factor.
        # So, we skip it and move to the next number.
        if prime[p]:

            # If prime[p] is True, then 'p' is a prime number.
            # Now, we need to mark all multiples of 'p' as non-prime (set their status to False).
            # We start marking multiples from p*p. Why not from 2*p or 3*p?
            # Because multiples like 2*p, 3*p, ..., (p-1)*p would have already been marked
            # False by their smaller prime factors (2, 3, ..., or (p-1)).
            # For example, if p=5, we start marking from 5*5=25.
            # 5*2=10 was marked by 2.
            # 5*3=15 was marked by 3.
            # 5*4=20 was marked by 2.
            # So, p*p is the first multiple of 'p' that hasn't necessarily been marked yet.
            for i in range(p * p, n + 1, p):
                prime[i] = False # Turn off the light for this multiple, it's not prime.

        # Move to the next number to check.
        # We increment 'p' by 1 to check the next integer.
        # (The loop condition `p * p <= n` will eventually stop the process).
        p += 1

    # Step 3: Collect all the numbers that are still marked as prime (True).
    # After the main sieve loop finishes, any number 'i' for which prime[i] is still True
    # means it was not crossed out by any smaller prime, and thus, it is a prime number itself.
    res = [] # Initialize an empty list to store our prime numbers.
    for p in range(2, n + 1): # We iterate from 2 up to 'n' (inclusive).
        if prime[p]: # If the light for 'p' is still ON (True)...
            res.append(p) # ...add 'p' to our list of prime numbers.

    return res # Return the list of all prime numbers found.

# This is a standard Python construct.
# It means the code inside this block will ONLY run when the script is executed directly.
# It will NOT run if this script is imported as a module into another Python file.
# This is useful for testing the function or providing example usage.
if __name__ == "__main__":
    # Define the upper limit 'n' for finding prime numbers.
    n = 35

    print(f"Finding prime numbers up to {n} using Sieve of Eratosthenes:")

    # Call our 'sieve' function with 'n' to get the list of prime numbers.
    res = sieve(n)

    # Print the prime numbers found.
    # 'end=" "' makes sure each number is printed on the same line, separated by a space.
    print("Prime numbers are:", end=' ')
    for ele in res:
        print(ele, end=' ')
    print() # Print a newline character at the end for clean output.

    # You can test with other numbers too:
    # print("\nPrime numbers up to 100:")
    # primes_100 = sieve(100)
    # for p_val in primes_100:
    #     print(p_val, end=' ')
    # print()

    # print("\nPrime numbers up to 2:")
    # primes_2 = sieve(2)
    # for p_val in primes_2:
    #     print(p_val, end=' ')
    # print()