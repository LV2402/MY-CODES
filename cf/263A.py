# Read the matrix input
matrix = []
for i in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

# Find the position of 1
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            # Calculate the number of moves to the center (3, 3)
            moves = abs(i + 1 - 3) + abs(j + 1 - 3)  # Adding 1 because i, j are 0-indexed
            print(moves)
            break
