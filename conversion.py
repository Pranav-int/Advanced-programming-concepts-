def decimal_to_binary(n):
    if n == 0:
        return ""
    
    return decimal_to_binary(n // 2) + str(n % 2)
num = 10

if num == 0:
    print("Binary: 0")
else:
    print("Binary:", decimal_to_binary(num))
