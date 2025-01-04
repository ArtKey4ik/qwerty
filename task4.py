try:
    start = int(input("Введіть початкове число (з): "))
    end = int(input("Введіть кінцеве число (по): "))

    if start > end:
        print("Помилка: початкове число має бути меншим або рівним кінцевому числу.")
    else:
        print("Числа у вказаному діапазоні:")
        for number in range(start, end + 1):
            print(number, end=" ")
        print()

except ValueError:
    print("Помилка: введіть коректні цілі числа.")
