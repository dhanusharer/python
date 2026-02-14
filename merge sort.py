def merge_sort(arr):
    if len(arr) > 1:  
        mid = len(arr) // 2  # Find the middle of the array
        left_half = arr[:mid]  # Divide the array into left half
        right_half = arr[mid:]  # Divide the array into right half

        merge_sort(left_half)  # Recursively sort the left half
        merge_sort(right_half)  # Recursively sort the right half

        merge(arr, left_half, right_half)  # Merge the sorted halves

def merge(arr, left_half, right_half):
    i = j = k = 0  # Initialize indices for left_half, right_half, and merged array

    # Merge elements from left_half and right_half into arr[]
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    # Copy any remaining elements of left_half
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    # Copy any remaining elements of right_half
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

# Example usage
arr = [34]
merge_sort(arr)
print("Sorted array:", arr)