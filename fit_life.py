# Проект FitLife - MVP версия 1.0

# 1. Знакомство
print("Добро пожаловать в FitLife!\n\n")
print("Для расчета показателей укажи свои данные.")
user_name = input("Имя: ")
try:
    user_age = int(input("Возраст: "))
except ValueError:
    print("Вы ввели недопустимое значение возраста.")
    print("Необходимо вводить целое число.")
    print("Повторите запуск программы.")
    exit()


# 2. Сбор данных
try:
    user_weight = float(input("Вес (в килограммах): "))
    user_height = float(input("Рост (в метрах, например 1.75): "))
except ValueError:
    print("Вы ввели недопустимое значение веса или роста.")
    print("Это должно быть число, разделитель точка.")
    print("Повторите запуск программы.")
    exit()

# 3. Логика расчетов
# Расчет ИМТ и округление до 1 знака
bmi = round((user_weight / user_height ** 2), 1)

# Расчет нормы воды в литрах и округление до 1 знака
water_needed = round((user_weight * 30 / 1000), 1)


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
