s = float(input('vamos calular seu aumento de salario! quanto voce ganha atualmente? R$ '))
if s > 1250:
    print(f'seu atual salario de {s}R$ com um aumento de 10% ficara em {s + (s * (10 / 100 )):.2f}R$')

else:
    print(f'seu salario atual de {s}R$ com um aumento de 15% ficara em {s + (s * (15 / 100 )):.2f}R$')
