import sys
a = [0,0]
while True:
    for i in a:
        x=0
        y=0
        b = int (input("Введите количество шагов(0 для остановки): "))
        if b == 0:
            sys.exit(a)
        if b < 0:
            sys.exit("Неверно введено количество шагов")
        c = input("Введите направление(стоп для остановки): ")
        if c == "стоп":
            sys.exit(a)
        if c!="вверх" and c!="вниз" and c!="вправо" and c!="влево":
            sys.exit("Неверное направление")
        if b > 0 and c =="вверх":
            y=+b
        if b > 0 and c =="вниз":
            y=-b 
        if b > 0 and c =="влево":
            x=-b         
        if b > 0 and c == "вправо":
            x=+b
        a=[a[0]+x, a[1]+y]
        print(a)
