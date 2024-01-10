def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def main():
    K1, K2 = map(int, input().split())
    message = input().strip()

    for c in message:
        ascii_value = ord(c)
        gcd_value = gcd(ascii_value, K1)
        encrypted_value = gcd_value % K2

        print(encrypted_value, end=" ")

if __name__ == "__main__":
    main()
