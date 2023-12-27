class Model:
    """Model class for the sorting algorithms"""
    def bubble_sort(arr):
        # Step 1: Iterate through the array
        n = len(arr)
        steps = []
        for i in range(n - 1):
            # Step 2: Compare adjacent elements and swap if necessary
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                steps.append(list(arr))  # Append current state of the array
        return steps

    
    def merge_sort(arr):
         # Step 1: Divide the array into two halves
         if len(arr) <= 1:
             return arr
         mid = len(arr) // 2
         left = arr[:mid]
         right = arr[mid:]
         # Step 3: Merge the sorted sub-arrays
         steps = []
         steps.extend(Model.merge_sort(left))
         steps.extend(Model.merge_sort(right))
         
         i = j = k = 0
         while i < len(left) and j < len(right):
             if left[i] < right[j]:
                 arr[k] = left[i]
                 i += 1
             else:
                 arr[k] = right[j]
                 j += 1
             k += 1
             steps.append(list(arr))  # Append current state of the array
         while i < len(left):
             arr[k] = left[i]
             i += 1
             k += 1
             steps.append(list(arr))  # Append current state of the array
         while j < len(right):
             arr[k] = right[j]
             j += 1
             k += 1
             steps.append(list(arr))  # Append current state of the array
         return steps

    def insertion_sort(arr):
        # Step 1: Iterate through the array
        steps = []
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            # Step 2: Move elements greater than key to the right
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            steps.append(list(arr))  # Append current state of the array
        return steps


    def quick_sort(arr):
        # Step 1: Choose a pivot element
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        # Step 2: Recursively sort the sub-arrays
        steps = []
        steps.extend(Model.quick_sort(left))
        steps.extend(middle)
        steps.extend(Model.quick_sort(right))
        return steps


    def bogo_sort(arr):
        import random

        def is_sorted(arr):
            for i in range(1, len(arr)):
                if arr[i] < arr[i - 1]:
                    return False
            return True

        # Step 1: Shuffle the array until it is sorted
        steps = []
        while not is_sorted(arr):
            random.shuffle(arr)
            steps.append(list(arr))  # Append current state of the array
        return steps

    
    