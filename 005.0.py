num = 21
while True:
    divisible = True
    for i in range(1, 21):
        if num % i != 0:
            num += 1
            divisible = False
            break
    if divisible:
        print(num)
        break
