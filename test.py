def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half,right_half)

def merge(left, right):
    merged = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])

    return merged

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr


unsorted_list_1 = []
n = int(input("Enter the number of elements[Merge Sort]: "))
for i in range(n):
    element = int(input(f"Enter Element {i+1} : "))
    unsorted_list_1.append(element)
    
unsorted_list_2 = []
n = int(input("Enter the number of elements[Insertion Sort]: "))
for i in range(n):
    element = int(input(f"Enter Element {i+1} : "))
    unsorted_list_2.append(element)
    

sorted_list_1 = merge_sort(unsorted_list_1)
print("Sorted list [Merge Sort]:", sorted_list_1)


sorted_list_2 = insertion_sort(unsorted_list_2)
print("Sorted list [Insertion Sort]:", sorted_list_2)
