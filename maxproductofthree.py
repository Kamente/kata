def solution(A):
    A.sort()
    n = len(A)

    product1 = A[n - 1] * A[n - 2] * A[n - 3]

    product2 = A[0] * A[1] * A[n - 1]

    product3 = A[n - 1] * A[n - 2] * A[n - 3]

    return max(product1, product2, product3)


A = [-3, 1, 2, -2, 5, 6]
result = solution(A)
print(result)
