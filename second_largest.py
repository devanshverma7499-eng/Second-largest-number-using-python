def second_largest(L):
    largest = L[0]
    second = L[0]

    for num in L:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return second


L = [10, 45, 20, 78, 34, 90, 56]

print("List =", L)
print("Second Largest =", second_largest(L))