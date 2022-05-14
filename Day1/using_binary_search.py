from bisect import bisect_left

def find_k(numbers, k):
    numbers.sort()
    for i in range(len(numbers)):
        target = k - numbers[i]
        j = binary_search(numbers, target)

        if j == -1:
            continue
        elif j != i:
            return True
        elif j+1 < len(numbers) and numbers[j+1] == k:
            return True
        elif j-1 >= 0 and numbers[j-1] == k:
            return True
    return False
    

def binary_search(numbers, target):
    lo = 0
    hi = len(numbers)
    ind = bisect_left(numbers, target, lo, hi)
    if 0 <= ind < hi and numbers[ind] == target:
        return ind
    return -1

numbers = [10, 15, 3, 7]
k = 17

print(find_k(numbers, k))