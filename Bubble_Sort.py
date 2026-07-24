def sort(array, size):
    for i in range(0, size-1):
        for j in range(0, size-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

array = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
size = len(array)

sort(array, size)

print(array)
