# Дополнительное практическое задание по модулю: "Основные операторы"
def find_divisors(number):
    pairs = []

    # Генерация всех возможных пар чисел в диапазоне от 3 до 20
    for i in range(1, number):
        for j in range(i + 1, number):
            if number % (i + j) == 0:
                pairs.append((i, j))
            #    print(i, j) для проверки выводим найденные пары


    return "".join([str(a[0])  +  str(a[1]) for a in pairs] ) #т.к. .join не работает с числовым форматом,
# при помощи str превращаем числа в строку и при помощи join обьединяем строки


for k in range (3, 21):
    result = find_divisors( k )
    print('k = ', k, 'result', result)