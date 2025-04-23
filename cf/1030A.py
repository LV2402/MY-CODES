# Input
n = int(input())  # Number of people
opinions = list(map(int, input().split()))  # Opinions: 0 (easy), 1 (hard)

# Check if any opinion is "hard"
if 1 in opinions:
    print("HARD")
else:
    print("EASY")
