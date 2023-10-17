def solution(A, K):
    if not A:
        return A
    N = len(A)
    rotated_array = [0] * N

    for i in range(N):
        new_index = (i + K) % N
        rotated_array[new_index] = A[i]

    return rotated_array


print(solution([0, 1, 2, 3], 5))
