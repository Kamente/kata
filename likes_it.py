# def likes(names):
#     if len(names) == 0:
#         return "no one likes this"
#     elif len(names) == 1:
#         return f"{names[0]} likes this"
#     elif len(names) == 2:
#         return f"{names[0]} and {names[1]} like this"
#     elif len(names) == 3:
#         return f"{names[0]}, {names[1]} and {names[2]} like this"
#     else:
#         others_count = len(names) - 2
#         return f"{names[0]}, {names[1]} and {others_count} others like this"


# print(likes([]))
# print(likes(["Peter"]))
# print(likes(["Jacob", "Alex"]))
# print(likes(["Max", "John", "Mark"]))
# print(likes(["Alex", "Jacob", "Mark", "Max"]))


def likes(names):
    if len(names) == 0:
        return "no one likes it"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} likes this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} likes this"
    else:
        others_count = len(names) - 2
        return f"{names[0]} and {names[1]} and {others_count} likes this"


print(likes(["Justin", "Lynn", "Dusty", "Kamente", "Dan"]))
