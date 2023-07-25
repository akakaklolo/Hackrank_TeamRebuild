def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        mergeSort(left_half)
        mergeSort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

n = int(input())
data = list(map(int, input().split()))
mergeSort(data)
Gia_tri_lon_nhat = max(data)
count = 0
for x in data:
    if x == Gia_tri_lon_nhat:
        count += 1
print(count)
#mergesort giá trị tìm giá trị lớn nhất
