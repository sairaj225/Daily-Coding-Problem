
def find_k(numbers, k):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j and numbers[i]+numbers[j] == k:
                return True
    return False


numbers = [10, 15, 3, 7]
k = 17

print(find_k(numbers, k))