altura = float(input('Digite sua altura em metros: '))
peso = float(input('Digite seu peso em kilogramas: '))
altura = altura**2
n1 = peso / altura
if n1 < 18.5:
    print('Abaixo do peso')
elif 18.6 < n1 < 26:
    print('Peso ideal')
elif 25 < n1 < 31:
    print('Sobrepeso')
elif 30 < n1 < 41:
    print('Obeso')
else:
    print('Obesidade mórbida')
