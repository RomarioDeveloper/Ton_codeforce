t = int(input())
for _ in range(t):
    n = int(input())
    a = []
    current = 1
    for i in range(1, n + 1):
        found = False
        for num in range(current, 101):
            mod_i = num % i
            if all(mod_i != (a[j] % (j + 1)) for j in range(len(a))):
                a.append(num)
                current = num + 1
                found = True
                break
        if not found:
            break
    print(' '.join(map(str, a)))