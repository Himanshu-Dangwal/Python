MOD = 1000000007

def count_ways(n):
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2

    return (count_ways(n - 1) % MOD + count_ways(n - 2) % MOD + count_ways(n - 3) % MOD) % MOD

if __name__ == "__main__":
    n = int(input("Enter the value of N: "))
    ways = count_ways(n)
    print("Number of ways to reach the top:", ways)
