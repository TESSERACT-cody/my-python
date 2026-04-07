def to_roman(n):
    values = [
        (1000, 'M'), (900, 'CM'),
        (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'),
        (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'),
        (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]
    
    result = ''
    
    for val, sym in values:
        while n >= val:
            result += sym
            n -= val
            
    print(result)


# пример использования
num = int(input("Введите натуральное число: "))
to_roman(num)
