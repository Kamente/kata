def duplicate_count(text):
    char_count = {}
    duplicates = 0

    for char in text:
        char_lower = char.lower()

        if char_lower.isalnum():
            if char_lower in char_count:
                char_count[char_lower] += 1
                if char_count[char_lower] == 2:
                    duplicates += 1
            else:
                char_count[char_lower] = 1
    return duplicates


print(duplicate_count("abcde"))
print(duplicate_count("aabbcde"))
print(duplicate_count("aabBcde"))
print(duplicate_count("indivisibility"))
print(duplicate_count("Indivisibilities"))
print(duplicate_count("aA11"))
print(duplicate_count("ABBA"))
