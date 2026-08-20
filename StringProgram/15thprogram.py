s = input("Enter string: ")

printed = ""

for ch in s:
    if s.count(ch) > 1 and ch not in printed:
        print(ch)
        printed += ch