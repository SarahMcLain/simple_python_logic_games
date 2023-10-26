def sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - 1 - 1):
            if arr[j] > arr[j +1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        if not swapped:
            break


numbers = [64, 34, 25, 12, 22, 11, 90]
sort(numbers)

print("Sorted array", numbers)