try:
    n = int(input("Введіть число n: "))

    if n < 1:
        print("Помилка: число n має бути більшим або рівним 1.")
    else:
        print("Парні числа у зворотному порядку:")
        for number in range(n, 0, -1):
            if number % 2 == 0:
                print(number, end=" ")
        print()

except ValueError:
    print("Помилка: введіть коректне ціле число.")
