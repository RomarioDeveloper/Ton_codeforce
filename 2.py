def solve(t, test_cases):
    results = []
    for s in test_cases:
        n = len(s)
        for i in range(n - 1):
            if s[i] != s[i + 1]:
                results.append(s[i:i + 2])
                break
        else:
            results.append("-1" if n == 1 else s)
    return results

t = int(input())
test_cases = [input().strip() for _ in range(t)]
print("\n".join(solve(t, test_cases)))
