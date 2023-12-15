def find_pythagorean_triplet(arr):
    arr = [x**2 for x in arr]
    arr.sort()

    for i in range(len(arr) - 1, 1, -1):
        left = 0
        right = i - 1

        while left < right:
            if arr[left] + arr[right] == arr[i]:
                return True
            elif arr[left] + arr[right] < arr[i]:
                left += 1
            else:
                right -= 1

    return False

def main():
    n = int(input())
    arr = list(map(int, input().split(" ")))

    if find_pythagorean_triplet(arr):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
