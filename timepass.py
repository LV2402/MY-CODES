ps, p, f, n = map(int, input("Enter Page Size, Pages, Frames, Addresses: ").split())
pt = [i if i < f else -1 for i in range(p)]
addrs = list(map(int, input("Enter Logical Addresses: ").split()))

print("\nPage -> Frame Mapping:")
for i in range(p):
    print(f"Page {i} -> {'Frame ' + str(pt[i]) if pt[i] != -1 else 'Not Mapped'}")

print("\nAddress Translation:")
for a in addrs:
    pg, off = a // ps, a % ps
    if pg >= p or pt[pg] == -1:
        print(f"Invalid address: {a}")
    else:
        pa = pt[pg] * ps + off
        print(f"Logical {a} => Physical {pa}")
