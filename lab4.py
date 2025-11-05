import time
# Insertion Sort implementation
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Merge Sort implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Get user input list
try:
    user_input = input("Enter your list of numbers separated by spaces: ")
    input_list = list(map(int, user_input.split()))
except ValueError:
    print("Invalid input. Using default list for demonstration.")
    input_list = [64, 34, 25, 5, 22]

# Display the user input
print("\nYour input list:", input_list)

# Perform and display insertion sort
start_time = time.time()
insertion_sorted = insertion_sort(input_list.copy())
end_time = time.time()
print("\nInsertion Sort result:", insertion_sorted)
print("Time taken for insertion sort: {:.6f} seconds".format(end_time - start_time))

# Perform and display merge sort
start_time = time.time()
merge_sorted = merge_sort(input_list.copy())
end_time = time.time()
print("\nMerge Sort result:", merge_sorted)
print("Time taken for merge sort: {:.6f} seconds".format(end_time - start_time))
print("Tejaswini-24303")
