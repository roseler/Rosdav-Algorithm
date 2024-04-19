def rosdav(arr):
    
    n = len(arr)
    # Returns the n th element of the array.
    if n <= 1:
        return arr
    else:
        mid = n // 2
        left = rosdav(arr[:mid])
        right = rosdav(arr[mid:])
        i, j, k = 0, 0, 0
        result = []
        # Append the elements of the left and right elements to the result.
        while i < len(left) and j < len(right):
            # Append the result to the result.
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
            k += 1
        # Append to result. append left to result.
        while i < len(left):
            result.append(left[i])
            i += 1
            k += 1
        # appends the result to the result.
        while j < len(right):
            result.append(right[j])
            j += 1
            k += 1
        # Returns a list of sorted results.
        if len(result) % 2 == 0:
            mid_idx = len(result) // 2
            return result[:mid_idx] + sorted(result[mid_idx:])
        else:
            mid_idx = len(result) // 2
            return result[:mid_idx+1] + sorted(result[mid_idx+1:])

arr = [9, 4, 6, 1, 3, 5, 8, 2, 7]
sorted_arr = rosdav(arr)
print(sorted_arr)
