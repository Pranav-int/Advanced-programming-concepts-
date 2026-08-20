from array import array

a = array('i', [10, 20, 30])

with open("data.bin", "wb") as f:
    a.tofile(f)

print("Data stored in file")