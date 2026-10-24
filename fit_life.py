# Проект FitLife - MVP версия 1.0

# Рекомендуемое количество мл воды на 1 кг массы тела
ML_PER_KG = int(30)
# Количество мл в 1 л
ML_PER_L = int(1000)


# 1. Знакомство
print("Добро пожаловать в FitLife!\n\n")
print("Для расчета показателей укажи свои данные.")
# Получение имени
user_name = input("Имя: ")

# Получение возраста
while True:
    try:
        user_age = int(input("Возраст: "))
        break
    except ValueError:
        print("Вы ввели недопустимое значение возраста.")
        print("Необходимо вводить целое число.")
        print("Повторите ввод.")


# 2. Сбор данных
# Получение веса
while True:
    try:
        user_weight = float(input("Вес (в килограммах): "))
        break
    except ValueError:
        print("Вы ввели недопустимое значение веса.")
        print("Это должно быть число, разделитель точка.")
        print("Повторите ввод.")

# Получение роста
while True:
    try:
        user_height = float(input("Рост (в метрах, например 1.75): "))
        break
    except ValueError:
        print("Вы ввели недопустимое значение роста.")
        print("Это должно быть число, разделитель точка.")
        print("Повторите ввод.")


# 3. Логика расчетов
# Расчет ИМТ и округление до 1 знака
bmi = round((user_weight / user_height ** 2), 1)

# Расчет нормы воды в литрах и округление до 1 знака
water_needed = round((user_weight * ML_PER_KG / ML_PER_L), 1)


# 4. Вывод красивого результата
print(f"\nПривет, {user_name}!")
print("Твои данные:")
print(f"Возраст: {user_age} лет")
print(f"Вес: {user_weight} кг.")
print(f"Рост: {user_height} м.")
print("\nДля тебя были рассчитаны показатели:")
print(f"Индекс массы тела (ИМТ): {bmi}")
print(f"Норма воды: {water_needed} л.\n")

print("Расчет окончен. Будьте здоровы!")
