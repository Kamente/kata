class Animal:
    def __init__(self, name, number_of_legs):
        self.name = name
        self.number_of_legs = number_of_legs


def sort_animals(lst):
    if not lst:
        return []

    sorted_animals = sorted(lst, key=lambda animal: (
        animal.number_of_legs, animal.name))

    return sorted_animals


animal1 = Animal("cat", 4)
animal2 = Animal("spider", 8)
animal3 = Animal("cow", 4)
animal4 = Animal("hen", 2)

animal_list = [animal1, animal2, animal3, animal4]
sorted_animals = sort_animals(animal_list)

for animal in sorted_animals:
    print(animal.name, animal.number_of_legs)
