print('Задача 1. Урок информатики 2')

# В прошлый раз учитель написал программу, которая выводит числа в формате плавающей точки, однако он вспомнил,
# что не учёл одну важную вещь: числа-то могут идти от нуля.

# Задано положительное число x (x > 0).
# Ваша задача — преобразовать его в формат плавающей точки, то есть x = a * 10 ** b  где 1 ≤ a < 10.
# Обратите внимание, что x теперь больше нуля, а не больше единицы. Обеспечьте контроль ввода.

# Пример 1
# Введите число: 92345
# Формат плавающей точки: x = 9.2345 * 10 ** 4

# Пример 2
# Введите число: 0.0012
# Формат плавающей точки: x = 1.2 * 10 ** -3

def find_ab(Float_num):
    degree_counter = 0
    if Float_num >= 10:
        while Float_num > 10:
            Float_num /= 10
            degree_counter += 1
        return Float_num, degree_counter
    elif Float_num < 1:
        while Float_num < 1:
            Float_num *= 10
            degree_counter -= 1
        return round(Float_num, 1), degree_counter
    else:
        degree_counter = 0
        return int(Float_num), degree_counter
    
def new_num():
    num = float(input("Введите число: "))
    if num <= 0:
        print("Число должно быть > 0.")
        return new_num()
    return num


result_a, result_b = find_ab(new_num())

print(f'Формат плавающей точки: x = {result_a} * 10 ** {result_b}')