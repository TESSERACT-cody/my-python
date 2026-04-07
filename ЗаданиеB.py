def task_b(number):
    # Преобразуем число в строку и выводим каждую цифру с новой строки
    for digit in str(number):
        print(digit)

# Пример использования:
num = int(input("Введите натуральное число: "))
task_b(num)
