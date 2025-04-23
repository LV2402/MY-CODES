# Read input
n = int(input())  # The number of stones
s = input()       # The string representing the stones

# Initialize a counter for the stones to remove
removals = 0

# Traverse the string and check each neighboring pair of stones
for i in range(1, n):
    if s[i] == s[i - 1]:  # If current stone is the same as the previous one
        removals += 1  # We need to remove one of them

# Print the total number of removals
print(removals)
