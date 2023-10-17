def solution(A):
    east_cars = 0
    passing_cars = 0

    for car in A:
        if car == 0:
            east_cars += 1
        else:
            passing_cars += east_cars
            if passing_cars > 1000000000:
                return -1

    return passing_cars


# A = [0, 1, 0, 1, 1]
# result = solution(A)
# print(result)

print (solution([0,1,0,1,1]))