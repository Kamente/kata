def solution(X, Y, D):
    distance = Y-X
    minimal_jumps = -(-distance // D)

    return minimal_jumps


print(solution(20, 40, 5))
