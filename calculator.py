a=int(input("Kérem az első számot: "))
b=int(input("Kérem a második számot: "))
c=input("Kérem a műveletet: ")
vege=input("További művelet?(y-nal tovább megy, exit-el kilép)")

while vege == "exit":
    if vege == "y":
        elif c == "+":
         d=a+b
         print(f'Az összeg: {d}')
        elif c == "-":
         d=a-b
         print(f'A kivonás: {d}')
        elif c == "*":
         d=a*b
         print(f'A szorzat: {d}')
        elif c == "/":
         d=a/b
         print(f'A hányados: {d}')
        break
print(f'{d}')
