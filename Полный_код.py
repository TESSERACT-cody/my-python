# Задача A
def task_a(n):
    print('-' * n)


# Задача B
def task_b(number):
    for digit in str(number):
        print(digit)


# Основная программа
print("Задача A")
n = int(input("Введите N: "))
task_a(n)

print("\nЗадача B")
num = int(input("Введите натуральное число: "))
task_b(num)
