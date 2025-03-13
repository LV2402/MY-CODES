def sieve(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False
    return [i for i in range(n + 1) if prime[i]]

def segment_sieve(a, b):
    primes = sieve(int(b**0.5))  # Find small primes up to √b
    is_prime = [True] * (b - a + 1)

    for p in primes:
        start = max(p * p, (a + p - 1) // p * p)  # Ensure we start marking from p^2 or a multiple >= a
        for j in range(start, b + 1, p):
            is_prime[j - a] = False

    if a == 1:  # 1 is not prime
        is_prime[0] = False

    for i in range(b - a + 1):
        if is_prime[i]:
            print(a + i)

for _ in range(int(input())):
    a, b = map(int, input().split())
    segment_sieve(a, b)
