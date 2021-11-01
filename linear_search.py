def linearsearch(arr, x):
    for i in range(0, len(arr)):
        if arr[i] == x:
            return i


if __name__ == "__main__":
    arr = []
    n = int(input("Enter no of element"))
    for j in range(0, n):
        ele = int(input())
        arr.append(ele)
    x = int(input("Enter the element to search"))
    result = linearsearch(arr, x)
    print("element present at index:", result)
