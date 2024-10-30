saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def validarNumero(num):
    if num.isnumeric():
        return float(num)
    else:
        print("Valor inválido.")
        return None

while True:
    print("[1] Depositar \n[2] Sacar \n[3] Extrato \n[4] Sair")
    menu = input("Escolha uma opção: ")
  
    if menu == "1":
        valor = input("Digite o valor a depositar: ")
        valor = validarNumero(valor)
        if valor is not None and valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"\nDepositado com sucesso! Saldo: R$ {saldo:.2f}\n")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif menu == "2":
        valor = input("Digite o valor a sacar: ")
        valor = validarNumero(valor)
        
        if valor is not None:
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")
            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print(f"\nSaque realizado com sucesso! Saldo: R$ {saldo:.2f}\n")
            else:
                print("Operação falhou! O valor informado é inválido.")
        else:
            continue

    elif menu == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("==========================================")

    elif menu == "4":
        print("Saindo...")
        break

    else:
        print("\nOpção inválida, por favor escolha uma opção válida.\n")
