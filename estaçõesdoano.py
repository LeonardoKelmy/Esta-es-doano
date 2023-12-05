# Estações do ano


# Apresentação
print('\n\t\t\t -- Estações do ano --\n')

# Entradas

mes = int(input('informe o mês: '))
dia = int(input('informe o dia do mês: '))

# Processamento

if (mes == 12 and dia >= 22) or (mes == 1 or mes == 2) or (mes == 1 or mes == 3 and dia <= 19):
    print('verão')
elif (mes == 3 and dia >= 20) or (mes == 4 or mes == 5 or mes == 6) or (mes == 4 or mes == 7 and dia <= 20):
    print('outono')
elif (mes == 7 and dia >= 21) or (mes == 7 or mes == 8) or (mes == 7 or mes == 9 and dia <= 22):
    print('Inverno')
elif (mes == 9 and dia >= 23) or (mes == 10 or mes == 11) or (mes == 10 or mes == 12 and dia <= 21):
    print('Primavera')
