import csv
from io import open
import msvcrt
import os
import os.path
# cadena = ['λ,S;q,A ', 'λ,AP;q,m n Z AP', 'λ,AP;q,epsilon', 'λ,A;q,x C AP', 'λ,A;q,y B AP', 'λ,ZP;q,r t Z ZP', 'λ,ZP;q,epsilon', 'λ,Z;q,1 ZP', 'λ,CP;q,q C CP', 'λ,CP;q,epsilon', 'λ,C;q,0 CP', 'λ,BP;q,p Z BP', 'λ,BP;q,epsilon']


# cadena = "# s d d s $ z z z z z $ λ,AP;q,m n Z AP"
 
# def writeArchivo(texto,ruta):
#     archivo  = open(f"{ruta}","a",encoding="utf-8")
#     texto = f"{texto}\n"
#     archivo.writelines(texto)
#     archivo.close()
    
# archivo = "z.csv"
# writeArchivo(cadena,archivo)
# x = 0
# cadena = "zMNz"
# while True:
#     letra = cadena[x]
#     print("Letra:"+letra)
#     if letra == "z":
#         print(cadena)
#         cadena = cadena.replace("z","",1)
#         cadena = cadena.strip()
#         cadena = cadena.rstrip("z")
#         print("Cadena:"+cadena)
#         print("Len:",len(cadena))
#         print(x)
#         x = -1
#     x +=1
#     print(x)
#     if x == len(cadena) :
#         break


lista = ["aMa"]

for cadena in lista:
    if cadena.find("") == 0:
        print(cadena)