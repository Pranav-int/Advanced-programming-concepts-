s = input("Enter string: ")

done = ""

for ch in s:
    if ch not in done:
        print(ch, "=", s.count(ch))
        done += ch