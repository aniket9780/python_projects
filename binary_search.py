def binarysearch(arr, l, r, x):
    if r >= l:
        mid = l + r // 2
        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binarysearch(arr, l, mid - 1, x)
        else:
            return binarysearch(arr, mid + 1, r, x)
    else:
        return -1


if __name__ == "__main__":
    arr = []
    n = int(input("ENTER NUMBER OF ELEMENT"))
    for i in range(0, n):
        ele = int(input())
        arr.append(ele)
    print("original array :", arr)
    arr.sort()
    print("Sorted array : ", arr)

    x = int(input("\n""Enter the element to search : "))
    result = binarysearch(arr, 0, len(arr) - 1, x)
    if result != -1:
        print("Element is present at index ", result)
    else:
        print("not present")
