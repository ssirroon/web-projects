def penis():
    num = int(input("Pick number: "))
    while num > 1:
        while num % 2 != 0:
            return False
        num = num // 2
    return True

print(penis())
