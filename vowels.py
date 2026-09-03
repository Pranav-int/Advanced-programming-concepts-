def count_vowels(text):
    count = 0
    vowels = "aeiouAEIOU"

    for char in text:
        if char in vowels:
            count += 1

    return count


text = input("Enter a string: ")
print("Number of vowels:", count_vowels(text))
