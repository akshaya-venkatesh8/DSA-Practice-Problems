def BinarySearch(arr, r, l, key) -> int:
    # print(r,l,arr[int((r+l) / 2)])
    if l >= r:
        return -1
    else:
        mid = int((r+l) / 2)
        # print(arr[mid] == key)
        if arr[mid] == key:
            # print(mid)
            return mid
        elif arr[mid] > key:
            return BinarySearch(arr, mid-1, l, key)
        else:
            return BinarySearch(arr, r, mid+1, key)


arr = [2,3,4,5,6,7,8,9,10]

val = BinarySearch(arr, len(arr)-1, 0, 4)
print(val)