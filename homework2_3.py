import sys
import math
a = float (input("Введите коэффициент a: "))
b = float (input("Введите коэффициент b: "))
c = float (input("Введите коэффициент c: "))
d = b*b-4*a*c
if d < 0:
    sys.exit("Корней нет")
if d == 0:
    x=-b/2*a
    print(f'Дискриминант: {d}')
    print(f'Корень уравения: {x}')
if d > 0:
    x1=(-b+math.sqrt(d))/(2*a)
    x2=(-b-math.sqrt(d))/(2*a)
    print(f'Дискриминант: {d}')
    print(f'Корни уравения: {x1}, {x2}')
