def traverse(arr):
    for elem in arr:
        print(elem, end=" ")
    print()

def insert(arr, index, value):
    return arr[:index] + [value] + arr[index:]

def delete(arr, index):
    return arr[:index] + arr[index+1:]

def linear_search_range(arr, value):
    for idx in range(len(arr)):
        if arr[idx] == value:
            return idx
    return -1

def update(arr, index, value):
    arr[index] = value
    return arr

# --------- User Input Section ---------
# Initial array
lst = list(map(int, input("Enter list elements separated by space: ").split()))
print("Original list:")
traverse(lst)

# Insert
index = int(input("Enter index to insert: "))
value = int(input("Enter value to insert: "))
lst = insert(lst, index, value)
print(f"After inserting {value} at index {index}:")
traverse(lst)

# Delete
del_index = int(input("Enter index to delete: "))
lst = delete(lst, del_index)
print(f"After deleting element at index {del_index}:")
traverse(lst)

# Linear search
search_value = int(input("Enter value to search: "))
idx_range = linear_search_range(lst, search_value)
print(f"Index of {search_value} (using range): {idx_range}")

# Update
update_index = int(input("Enter index to update: "))
update_value = int(input("Enter new value: "))
lst = update(lst, update_index, update_value)
print(f"After updating index {update_index} to {update_value}:")
traverse(lst)
print("Tejaswini-24303")
