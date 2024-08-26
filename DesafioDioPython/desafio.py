

# Depositos saque, deposito e extrato

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0 
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

def deposito():
    global saldo
    global extrato
    saldo += int(input("Digite o valor que deseja depositar: "))
    extrato.append(f"Depósito: {saldo}" )

def saque():
    global saldo
    global numero_saques
    global LIMITE_SAQUES
    global extrato

    if(saldo > 0):
        if(numero_saques == LIMITE_SAQUES ):
            print("Você atingiu o limite de saques")
        else:
            valorDesejadoSacar = int(input(f"Qual o valor que você deseja sacar? "))
            if(valorDesejadoSacar > 500):
                print("Você não tem permissão para sacar esse valor!")
            else:
                saldo -= valorDesejadoSacar
                numero_saques += 1
                extrato.append(f"Saque: {saldo}")
    else:
        print(f"Você não possui dinheiro!")

def exibirExtrato():
    global extrato
    global saldo
    for extratos in extrato:
        print(extratos)
       

    print(f"Saldo atual: {saldo}")

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        deposito()
    elif opcao == "s":
        print("Saque")
        saque()
    elif opcao == "e":
        print("Extrato")
        exibirExtrato()
    elif opcao == "q":
        break
    else:
        print("Operação invalida, por favor selecione novamente a opção desejada.")

