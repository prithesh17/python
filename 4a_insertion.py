def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr

unsorted_list = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    element = int(input(f"Enter Element {i+1} : "))
    unsorted_list.append(element)
sorted_list = insertion_sort(unsorted_list)
print("Sorted list:", sorted_list)
