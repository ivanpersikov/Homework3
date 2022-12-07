import sys
a = [0,0]
b = int (input("Введите количество шагов: "))
if b < 0:
    sys.exit("Неверно введено количество шагов")
c = input("Введите направление: ")
if c!="вверх" and c!="вниз" and c!="вправо" and c!="влево":
    sys.exit("Неверное направление") 
for i in [0,0]:
    if b > 0 and c =="вверх":
        a[1]=+b
    if b > 0 and c =="вниз":
        a[1]=-b 
    if b > 0 and c =="влево":
        a[0]=-b         
    if b > 0 and c == "вправо":
        a[0]=+b
print(a)


