'''
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним, только если треугольник существует .
Пример:

На входе:
a = 4
b = 4
c = 4

На выходе:
Треугольник существует
Треугольник равносторонний

Треугольник существует
Треугольник равнобедренный

Треугольник существует
Треугольник разносторонний

Треугольник не существует
'''
a = 4
b = 4
c = 4

if a==b==c:
    print('Треугольник существует')
    print('Треугольник равносторонний')
elif a+b < c or a+c < b or c+b < b:
    print('Треугольник не существует')
elif a+b > c or a+c > b or c+b > b:
    if a==b or a==c or b==c:
        print('Треугольник существует')
        print('Треугольник равнобедренный')
    elif a!=b!=c:
        print('Треугольник существует')
        print('Треугольник разносторонний')
    else:
        print('Треугольник не существует')