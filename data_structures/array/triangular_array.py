M = 10
for r in range(M):
    for c in range(M):
        if c > r:
            break
        i = int((r**2 + r) / 2 + c)
        print(f'{i}', end=" ")
    print()