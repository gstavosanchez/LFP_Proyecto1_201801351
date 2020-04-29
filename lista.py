import csv
cadena = ['λ,S;q,A ', 'λ,AP;q,m n Z AP', 'λ,AP;q,epsilon', 'λ,A;q,x C AP', 'λ,A;q,y B AP', 'λ,ZP;q,r t Z ZP', 'λ,ZP;q,epsilon', 'λ,Z;q,1 ZP', 'λ,CP;q,q C CP', 'λ,CP;q,epsilon', 'λ,C;q,0 CP', 'λ,BP;q,p Z BP', 'λ,BP;q,epsilon']


myData = [["first_name", "second_name", "Grade"],
          ['Alex', 'Brian', 'A'],
          ['Tom', 'Smith', 'B']]
 
myFile = open('example2.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)
     
print("Writing complete")