cadena = ['λ,S;q,A ', 'λ,AP;q,m n Z AP', 'λ,AP;q,epsilon', 'λ,A;q,x C AP', 'λ,A;q,y B AP', 'λ,ZP;q,r t Z ZP', 'λ,ZP;q,epsilon', 'λ,Z;q,1 ZP', 'λ,CP;q,q C CP', 'λ,CP;q,epsilon', 'λ,C;q,0 CP', 'λ,BP;q,p Z BP', 'λ,BP;q,epsilon']
x = 0 
y = 0
print()
for valor in cadena:
    valor = valor.strip()
    if valor.find("λ,A;")  - 1:
      y += 1
print(y)

for valor in cadena:
    valor = valor.strip()
    if valor.find("λ,A;") == 0:
      x += 1
      
print(x)  