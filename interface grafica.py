import PySimpleGUI as psg


# Função para determinar a estação do ano
def determinar_estacao(mes, dia):
    if (mes == 12 and dia >= 22) or (mes == 1 or mes == 2) or (mes == 1 or mes == 3 and dia <= 19):
        return 'Verão'
    elif (mes == 3 and dia >= 20) or (mes == 4 or mes == 5 or mes == 6) or (mes == 4 or mes == 7 and dia <= 20):
        return 'Outono'
    elif (mes == 7 and dia >= 21) or (mes == 7 or mes == 8) or (mes == 7 or mes == 9 and dia <= 22):
        return 'Inverno'
    elif (mes == 9 and dia >= 23) or (mes == 10 or mes == 11) or (mes == 10 or mes == 12 and dia <= 21):
        return 'Primavera'


# Layout da interface gráfica
layout = [
    [psg.Text('Informe o mês e o dia:')],
    [psg.Text('Mês:'), psg.Input(key='mes',size=(5,1))],
    [psg.Text('Dia:'), psg.Input(key='dia',size=(5,1))],
    [psg.Button('Determinar Estação'), psg.Button('Sair')],
    [psg.Text(size=(30, 1), key='saida')]
]

# Criar a janela
window = psg.Window('Estações do Ano', layout)

# Event Loop
while True:
    evento, valores = window.read()

    if evento in (psg.WINDOW_CLOSED, 'Sair'):
        break
    if evento == 'Determinar Estação':
        try:
            mes = int(valores['mes'])
            dia = int(valores['dia'])
            estacao = determinar_estacao(mes, dia)
            window['saida'].update(f'Estação do ano: {estacao}')
        except ValueError:
            window['saida'].update('Por favor, insira valores numéricos para mês e dia.')

# Fechar a janela
window.close()
