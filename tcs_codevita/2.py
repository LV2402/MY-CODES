import math

def polygon_area(x, y, n):
    s = 0.0
    for i in range(n):
        j = (i + 1) % n
        s += x[i] * y[j] - x[j] * y[i]
    return abs(s) / 2.0

def main():
    N = int(input().strip())
    x = []
    y = []
    for _ in range(N):
        xi, yi = map(float, input().split())
        x.append(xi)
        y.append(yi)

    per = 0.0
    lengths = [0]*N
    for i in range(N):
        j = (i + 1) % N
        L = abs(x[i] - x[j]) + abs(y[i] - y[j])
        lengths[i] = L
        per += L

    A0 = polygon_area(x, y, N)
    best = 0.0

    for k in range(1001):
        H = k / 10.0
        invalid = False

        for L in lengths:
            if L - 2 * H < 0.1 - 1e-12:
                invalid = True
                break

        if invalid:
            break

        A = A0 - per * H + 4.0 * H * H
        if A <= 0:
            break

        V = A * H
        if V > best:
            best = V

    print("{:.2f}".format(best), end="")  

if __name__ == "__main__":
    main()
