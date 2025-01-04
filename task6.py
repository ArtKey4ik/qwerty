try:
    n = int(input("Факторіал n: "))

    if n < 0:
        print("Помилка: число n має бути невід'ємним.")
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        print(f"Факторіал числа {n} дорівнює {factorial}.")

except ValueError:
    print("Помилка: введіть коректне ціле число.")
