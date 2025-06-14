def binary_search(arr, target):
    if not arr:
        return 0, None
    
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] == target:
            upper_bound = arr[mid]
            j = mid - 1
            while j >= 0 and arr[j] == target:
                upper_bound = arr[j]
                j -= 1
            return iterations, upper_bound
        elif arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1

    if left < len(arr):
        upper_bound = arr[left]
    return iterations, upper_bound

# Тестування
if __name__ == "__main__":
    arr = [1.1, 2.2, 3.3, 4.4, 5.5]
    test_targets = [3.0, 3.3, 6.0, 0.0]
    print("Результати двійкового пошуку:")
    for target in test_targets:
        result = binary_search(arr, target)
        print(f"Ціль: {target}, Ітерацій: {result[0]}, Верхня межа: {result[1]}")