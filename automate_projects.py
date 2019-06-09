def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1


user_int = int(input("Please provide a number.\n"))
loop_num = user_int

while True:
    if loop_num == 1:
        break
    else:
        loop_num = collatz(loop_num)
