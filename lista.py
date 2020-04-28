cadena = "z a z a b z b z"
cadena = cadena.split(" ")
x=0
while True:
    letra = cadena[x]
    print("Letra:",letra," Pos:",x)
    x+=1
    if x == len(cadena):
        print("x:",x)
        print(len(cadena))
        break
