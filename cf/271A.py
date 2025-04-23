def has_distinct_digits(year):
    return len(set(str(year))) == len(str(year))

def find_next_distinct_year(y):
    y += 1
    while not has_distinct_digits(y):
        y += 1
    return y

# Input
y = int(input())
# Output
print(find_next_distinct_year(y))
