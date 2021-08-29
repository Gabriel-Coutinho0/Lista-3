nota = float(input('nota: '))
while nota <0 or nota> 10:
    nota = float(input('Nota invalida, digite novamente:'))
else:
    print (f'{nota}')
