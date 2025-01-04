import random
secret_number = random.randint(1, 10)
attempts = 3  # Кількість спроб
print("Гра 'Вгадай число'!")
print("Я загадав число від 1 до 10. Спробуй його вгадати. У тебе є 3 спроби.")
for attempt in range(1, attempts + 1):
    try:
        guess = int(input(f"Спроба {attempt}. Введи своє число: "))
        if guess < secret_number:
            print("Більше")
        elif guess > secret_number:
            print("Менше")
        else:
            print(f"Вітаю! Ти вгадав число {secret_number} з {attempt} спроби!")
            break
    except ValueError:
        print("Будь ласка, введи ціле число від 1 до 10.")
else:
    print(f"На жаль, ти програв. Загадане число було {secret_number}.")
