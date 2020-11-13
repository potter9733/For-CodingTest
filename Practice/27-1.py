
def count(arr, x):
    from bisect import bisect_left, bisect_right
    left = bisect_left(arr, x)
    right = bisect_right(arr, x)
    
    return right - left

print(count([1,2,2,3,4,5,6], 2))