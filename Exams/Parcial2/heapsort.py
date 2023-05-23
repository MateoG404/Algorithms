
def heapify(arr, n, i):
    largest = i  
    left = 2 * i + 1     
    right = 2 * i + 2     
  
    if left < n and arr[i] < arr[left]:
        largest = left
  
    if right < n and arr[largest] < arr[right]:
        largest = right
  
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]  # swap
  
        heapify(arr, n, largest)
  
def heapSort(arr):
    n = len(arr)
  
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    
    print("heapfy",arr)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # swap
        heapify(arr, i, 0)

arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)

print("Lista ordenada:")
print(arr)
