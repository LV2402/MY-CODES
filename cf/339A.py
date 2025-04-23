# Read input
s = input()

# Split the string by '+' and sort the numbers
numbers = s.split('+')
numbers.sort()

# Join the sorted numbers with '+' and print the result
print('+'.join(numbers))
