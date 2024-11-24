def solve(t, test_cases):
    results = []
    for x, m in test_cases:
        count = 0
        y = 1
        while y <= m:
            if (x ^ y) % x == 0 or (x ^ y) % y == 0:
                count += 1
            y += x
        results.append(count)
    return results

# Чтение входных данных
t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

results = solve(t, test_cases)
print("\n".join(map(str, results)))
