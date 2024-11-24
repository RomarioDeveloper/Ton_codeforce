def solve():
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    results = []
    index = 1

    def find_divisors(n):
        divisors = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        return divisors

    for _ in range(t):
        x, m = map(int, data[index:index + 2])
        index += 2

        divisors = find_divisors(x)
        count = 0

        for z in divisors:
            y = z ^ x
            if 1 <= y <= m and y != x:
                count += 1

        results.append(count)

    sys.stdout.write('\n'.join(map(str, results)) + '\n')
