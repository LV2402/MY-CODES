from itertools import combinations

for _ in range(int(input())):
    n = int(input())
    s = input()

    first_half = s[:n]   # First n characters
    second_half = s[n:]  # Last n characters

    sub = []
    
    for a in combinations(first_half, 2):
        for b in combinations(second_half, 2):
            sub.append(''.join(a + b))

    print(sub)  # Print or process subsets as needed
