#Desafio de projeto DIO - Fundamentos de Python
#Sistema bacário básico com um único cliente, sendo possível sacar, depositar, verificar extrato.

#menu inicial com as opções disponíveis
menu = """
########################################
Escolha a opção desejada:

[s] Saque
[d] Depósito
[e] Extrato
[q] Sair

=> """


limite_saque = 500 #limite de valor para cada operação de saque
saldo = 0 #saldo inicial da conta
LIMITE_SAQUES = 3 #limite de saques
extrato = "" #criação da variável extrato
numero_saques = 0 #número de saques inicial

while True: #Roda o programa até o usuário solicitar sair

    opcao = input (menu) #Entrada da opção do usuário

    if opcao == "q": #Quando a opção for "q" o programa encerra
        break

    elif opcao == "s": #Quando a opção for "s" será para sacar

        valor = round (float (input ("Informe o valor do saque: ")),2) #Entrada do valor solicitado para saque, tranformado em float e com duas casas decimais
        
        #Verificação de critérios estabelecidos no projeto
        excedeu_limite = valor > limite_saque #O valor solicitado não pode ser maior que o limite de saque
        excedeu_saques = numero_saques >= LIMITE_SAQUES #A quantidade de saques realizadas dever ser no máximo 3
        excedeu_saldo = valor > saldo #Tem que ter saldo suficiente na conta para realizar o saque

        if excedeu_limite: #Se exceder o limite por saque a operação falha
            print ("Operação falhou. O valor solicitado excedeu o limite.")

        elif excedeu_saques: #Se exceder 3 saques a operação falha
            print ("Operação falhou. Número de saques diários execedido.")

        elif excedeu_saldo: #Se não tiver saldo suficiente a operação falha
            print ("Operação falhou. Saldo insuficiente.")

        elif valor > 0: #Se o valor solicitado for positivo inicia o processo de saque
            saldo -= valor #Diminui o valor solicitado para saque do saldo
            extrato += f"Saque: R$ {valor:.2f}\n" #Inclui a operação de saque no extrato
            numero_saques += 1 #Contabiliza mais um saque realizado
            print ("Saque realizado com sucesso") #Informa que o saque foi realizado

        else: #Caso o valor solicitado não se enquadre nos critérios estabelecidos a operação falha
            print ("Operação falhou. O valor informado é inválido.")

    elif opcao == "d": #Quando a opção for "d" será para depositar

        valor = round (float (input ("Informe o valor do depósito: "))) #Entrada do valor solicitado para depósito, tranformado em float e com duas casas decimais

        if valor > 0: #Se o valor para depósito for positivo inicia o processo de depósito
            saldo += valor #Aumenta o valor depositado ao saldo
            extrato += f"Depósito: R$ {valor:.2f}\n" #Inclui a operação de depósito no extrato
            print ("Depósito realizado com sucesso") #Informa que o depósito foi realizado

        else: #Caso o valor para depósito não se enquadre nos critérios estabelecidos a operação falha
            print ("Operação falhou. O valor informado é inválido.")

    elif opcao == "e": #Quando a opção for "e" será exibido o extrato
        print("\n################ EXTRATO ################") 
        print("Não foram realizadas movimentações." if not extrato else extrato) #Verifica se o extrato está vazio, caso positivo, exibe a primeira parte, caso contrário, exibe o extrato
        print(f"\nSaldo: R$ {saldo:.2f}") #Exibe o saldo com duas casas decimais
        print("############################################")

    else: #Caso a opção escolhida não se enquadre nas exibidas no menu exibe a mensagem
        print ("Opção inválida. Escolha uma opção válida.")