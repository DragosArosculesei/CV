with open('Adventofcode1.txt', 'r') as file:
   lines = file.readlines()

suma = 0 

for line in lines:
    number = 0
    s = line
    for i in s:
       if i.isnumeric():
            number = number*10 + int(i)
            break
    for i in reversed(s):
       if i.isnumeric():
            number = number*10 + int(i)
            break
    suma = suma + number
print(suma)