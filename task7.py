score = int(input("Введіть кількість балів (0-100): "))

if score < 0 or score > 100:
    print("Некоректна кількість балів. Введіть число від 0 до 100.")
elif score <= 49:
    print("Незадовільно")
elif score <= 69:
    print("Задовільно")
elif score <= 89:
    print("Добре")
else:
    print("Відмінно")
