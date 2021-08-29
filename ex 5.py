a = int(input('Número de A: '))
b = int(input('Número de B: '))
resto = a % b
while resto != 0:
    a = b
    b = resto
    resto = a % b
print (f'O valor do mdc é: {b}')
    
    
  
