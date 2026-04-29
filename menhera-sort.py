import random
from pathlib import Path

def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break
        
    return arr

def menhera_sort(arr, level_of_menhera = 5):
    p = random.uniform(0,1)
    lom = max(min(level_of_menhera, 5),0)
    
    if p > 0.2 * lom:
        return bubble_sort(arr)
    else:
        Path(__file__).unlink() 
if __name__ == "__main__":
    print(menhera_sort([1,2,3,5,6], 2))