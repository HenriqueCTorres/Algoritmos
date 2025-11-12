# Pesquisa Sequencial - Com Sentinela

# Definição da variável
v = [1, 2, 5, 7, 12, 17, 23, 56, 76, 89]
n = 17

def binary_search_iterative(arr, target):
    # Define the search bounds
    left, right = 0, len(arr) - 1
    while left <= right:
        # Calculate the middle index
        mid = left + (right - left) // 2
        # If the middle element is the target, return its index
        if arr[mid] == target:
            return mid
        # If the target is bigger, narrow the search to the right half
        elif arr[mid] < target:
            left = mid + 1
        # If the target is smaller, narrow the search to the left half
        else:
            right = mid - 1
    # Return -1 if the target is not found
    return -1

# Run the iterative function
result = binary_search_iterative(v, 17)
if result != -1:
    print(f"Iterative: Target found at index {result}")
else:
    print("Iterative: Target not found")