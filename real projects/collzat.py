def collzat(number):
    if number%2 == 0:
        return number // 2
    else:
        return 3 * number + 1

user_input = int(input("pls input an integer: "))

result = collzat(user_input)


while True:
    if result > 1:
        print(result)
        collzat(result)
        result = collzat(result)
        if result == 1:
            print(result)
    else:
        break
