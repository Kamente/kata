def solution(N):
    max_gap = 0
    current_gap = 0
    binary = bin(N)[2:]

    for digit in binary:
        if digit == '0':
            current_gap += 1
        else:
            max_gap = max(max_gap, current_gap)
            current_gap = 0

    return max_gap


print(solution(15))
print(solution(1041))

# array= {"H", "J"}
# for name in array:
#     print (name)