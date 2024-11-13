print('Задача 3. Число наоборот')

# Пользователь вводит два числа: N и K.
# Напишите программу, которая переворачивает каждое из введённых чисел, то есть записывает эти числа в обратном порядке.

# Пример
# Введите первое число: 102
# Введите второе число: 123

# Первое число наоборот: 201
# Второе число наоборот: 321

def new_nums():
    first_num, second_num = int(input("Введите первое число: ")), int(input("Введите второе число: "))
    return first_num, second_num

def reverse_num(first_num, second_num):
    first_num, second_num = str(first_num), str(second_num)
    first_num, second_num = int(first_num[-1::-1]), int(second_num[-1::-1])
    return(first_num, second_num)

first_result, second_result = reverse_num(*new_nums())

print("Первое число наоборот:", first_result)
print("Второе число наоборот:", second_result)