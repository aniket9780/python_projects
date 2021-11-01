def bubblesort(arr):
    m = len(arr)
    for i in range(m):
        for j in range(0, m - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    arr = []
    n = int(input("Enter the number of element"))
    for i in range(0, n):
        ele = int(input())
        arr.append(ele)
    print(arr)
    result = bubblesort(arr)
    print(result)
