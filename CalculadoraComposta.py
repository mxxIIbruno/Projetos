from time import sleep

entrada = float(input('Entrada: R$'))
mensal = float(input('Mensal: R$'))
total = float(input('Até quantos? R$'))

CDI = 0.1315
guardado_no_banco = entrada
cont = 0

cdi_anual = guardado_no_banco * CDI
cdi_mensal = cdi_anual / 12

ano = 0

print(f'Plano final: R${total:,.2f}\n')

while guardado_no_banco <= total:
    cdi_anual = guardado_no_banco * CDI
    cdi_mensal = cdi_anual / 12

    cont += 1

    if cont % 12 == 0:
        ano += 1

    print(f'No {cont}º mês.')
    print(f'\nCDI p/ ano: R${cdi_anual:,.2f}')
    print(f'CDI p/ mês: R${cdi_mensal:,.2f}')

    guardado_no_banco += cdi_mensal

    print(f'\nGanhou R${guardado_no_banco:,.2f}')
    print(f'\nDepositou: R${mensal:,.2f}')

    guardado_no_banco += mensal

    sleep(1)
    print('===='*8)

print(f'Você conquistou R${guardado_no_banco:,.2f} em\n{ano} ano(s) {cont % 12} mês(es)')
