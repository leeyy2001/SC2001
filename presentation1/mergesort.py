def mergeSort(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # Into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        comparisons_l = mergeSort(L)
 
        # Sorting the second half
        comparisons_r = mergeSort(R)
 
        i = j = k = 0
        comparisons = comparisons_l + comparisons_r

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            comparisons += 1
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        
        return comparisons

    return 0


