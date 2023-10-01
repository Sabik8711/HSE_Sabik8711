a=int( 78 )
b=float( 9.8)
c=bool( True)
id(a)

a=input("Введите число:")
if a.isdigit():
    seconds=int(a)
    minutes=seconds/60
    hours=minutes/60
    print (seconds)
    print(minutes)
    print(hours)


a=input("Введите число от 1 до 9: ")
if a.isdigit() and 0<int(a)<10:
    b=int(a)+int(a+a)+int(a+a+a)
    print(b)
