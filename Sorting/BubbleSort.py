def BubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]


arr = [10,60,29,4,23,89]

print(arr)
BubbleSort(arr)
print(arr)
for i in range(len(arr)):
    print(arr[i], end=",")