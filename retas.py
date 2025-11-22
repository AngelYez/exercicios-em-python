r1 = float(input('informe a primeira reta: '))
r2 = float(input('informe a segunda reta: '))
r3 = float(input('informe a terceira reta: '))

# BLOCO PARA VERIFICAR SE PODE FORMAR A RETA

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print(f'as tres retas {r1}, {r2} e {r3} podem formar um triangulo! ')

else:
    print(f'as tres retas {r1}, {r2} e {r3} nao podem formar um triangulo ')
