def count_pairs(arr, k):
    count = 0

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == k:
                count += 1

    return count


if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    print(count_pairs(arr, k))
