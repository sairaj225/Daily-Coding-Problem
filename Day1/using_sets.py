
def find_k(numbers, k):
    seen = set()
    for number in numbers:
        if k-number in seen:
            return True
        else:
            seen.add(number)
    return True


numbers = [10, 15, 3, 7]
k = 17

print(find_k(numbers, k))