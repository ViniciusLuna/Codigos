valor1 = int(input ("Digite primeiro numero: "))
valor2 = int(input("Digite o segundo nuemro: "))

operacao = input("Digite a operacao desejada: ")

print("Operacao escolhida foi " + operacao)

if(operacao == 'soma'):
    print("Operacao escolhida foi soma")
    print(valor1 + valor2)

if(operacao == 'Subtracao'):
    print("Operacao escolhida foi Subtracao")
    print(valor1 - valor2)

if(operacao == 'Multiplicacao'):
    print("Operacao escolhida foi multiplicacao")
    print(valor1 * valor2)

if(operacao == 'Divisao'):
    print("Operacao escolhida foi divisao")
    print(valor1 / valor2)
