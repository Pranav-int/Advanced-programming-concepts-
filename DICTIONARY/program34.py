text = input("Enter a string: ")

frequency = {}

for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

for ch in text:
    if frequency[ch] > 1:
        print("First repeating character:", ch)
        break