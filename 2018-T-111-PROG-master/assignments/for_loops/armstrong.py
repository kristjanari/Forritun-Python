top_num = int(input("Input a number between 0 and 999: "))

for i in range(0, top_num):
    if (i < 10):
        num_digits = 1
        third = 0
        second = 0
        first = i
    elif (i < 100):
        num_digits = 2
        third = 0
        second = i // 10
        first = i % 10
    else:
        num_digits = 3
        third = i // 100
        second = (i % 100) // 10
        first = (i % 100) % 10
    if (third**num_digits + second**num_digits + first**num_digits == i):
        print(i)


