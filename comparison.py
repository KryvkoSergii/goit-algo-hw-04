import random
import timeit

def generate(size):
    return [random.randint(0, 1000) for i in range(0, size)]

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key
    return lst

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def insert_sorting(arr):
        return timeit.timeit( 
            setup = '''from __main__ import insertion_sort''',
            stmt = f'''insertion_sort({arr})''',  
            number = 5)

def timsorting(arr):
        return timeit.timeit( 
            setup = '''from __main__ import generate''',
            stmt = f'''sorted({arr})''',  
            number = 5)

def merge_sorting(arr):
        return timeit.timeit(
            setup = '''from __main__ import merge_sort''',
            stmt = f'''list = merge_sort({arr})''',  
            number = 5)

def main():
    test_number(100)
    test_number(1000)
    test_number(10000)

def test_number(num):
    arr = generate(num)
    print(f"========= Test for {num} =========")
    timsort_res = timsorting(arr)
    print(f"Timsort time ({num}): {timsort_res}")
    merge_sorting_res = merge_sorting(arr)
    print(f"Merge sort time ({num}): {merge_sorting_res}")
    insert_sorting_res = insert_sorting(arr)
    print(f"Insertion sort time ({num}): {insert_sorting_res}")
    print(f"comparison merge source/timsort {merge_sorting_res*100/timsort_res} %")
    print(f"comparison insert sorting/timsort {insert_sorting_res*100/timsort_res} %")
    print(f"==================================")
     

if __name__ == "__main__":
    main()