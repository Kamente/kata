def solution(A):
    distinct_values = set()
    for value in A:
        distinct_values.add(value)
    return len(distinct_values)


print(solution([5, 5, 5, 6, 7]))
