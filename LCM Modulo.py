MOD = 10**9 + 7

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def lcm(a, b):
    return (a // gcd(a, b)) * b

def main():
    N = int(input())
    arr = list(map(int, input().split()))

    result = 1
    for i in range(N):
        for j in range(i + 1, N):
            result = (result * lcm(arr[i], arr[j])) % MOD

    print(result)

if __name__ == "__main__":
    main()
