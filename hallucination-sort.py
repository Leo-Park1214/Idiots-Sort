# if you using this sort argorithm 

import random

def hallucination_sort(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break

        r_idx = random.randrange(n)
        arr[r_idx] = random.uniform(min(arr), max(arr))
        
    return arr
if __name__ == "__main__":
    print(hallucination_sort([1,42,15,53,2]))