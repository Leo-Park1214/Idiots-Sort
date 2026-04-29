# If you provide this sorting algorithm with an unsorted list, it will delete that list!

def is_sorted(arr, ascending = True):
    for i in range(len(arr) - 1):
        if ascending:
            if arr[i] > arr[i + 1]:
                return False
        else:
            if arr[i] < arr[i + 1]:
                return False
    return True

def alpha_male_sort(arr):
    if is_sorted(arr, ascending = True) or is_sorted(arr, ascending = False):
        return arr
    else:
        arr.clear()
        return 


if __name__ == "__main__":
   print(alpha_male_sort([1, 2, 3, 4]))
