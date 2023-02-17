#INTRODUÇÃO

from database.db import *

def verifica_cpf(opcao, cpf):
    cursor.execute("SELECT * FROM Clientes")
    clientes = cursor.fetchall()
    
    if opcao == 1:
        for cliente in clientes:
            while cpf in cliente:
                print("\nCPF JÁ CADASTRADO!\n")
                cpf = str(input("CPF: "))
                
        return cpf
    
    elif opcao == 3 or opcao == 4:
        for cliente in clientes:
            while cpf not in cliente:
                print("\nCPF INEXISTENTE!\n")
                cpf = str(input("CPF (XXX.XXX.XXX-XX): "))
            
        return cpf

#MENU PRINCIPAL

print(36 * "-")
print("\tSISTEMA CRUD-MYSQL")
print(36 * "-")

while True:
    print("\nMENU PRRINCIPAL:\n")

    print("\t[1] CADASTRAR \n\t[2] LISTAR\n\t[3] ATUALIZAR\n\t[4] DELETAR\n\t[5] SAIR\n")

    opcao = int(input("SUA OPÇÃO: "))

    while 1 > opcao > 5:
        print("\nOPÇÃO INVÁLIDA!\n")
        
        print("\nMENU PRRINCIPAL:\n")

        print("\t[1] CADASTRAR \n\t[2] LISTAR\n\t[3] ATUALIZAR\n\t[4] DELETAR\n\t[5] SAIR\n")

        opcao = int(input("SUA OPÇÃO: "))
        
    #CREATE

    if opcao == 1:
        while True:
            print("\nCADASTRO DE CLIENTES\n")
            
            cpf = str(input("CPF (XXX.XXX.XXX-XX): "))
            
            cpf = verifica_cpf(opcao, cpf)    
            
            print()
            
            nome_completo = str(input("NOME COMPLETO: "))
            
            print()
            
            sexo = str(input("SEXO: "))
            
            print()
            
            data_nascimento = str(input("DATA DE NASCIMENTO (DD/MM/AAAA): "))
            
            print()
            
            data_nascimento = data_nascimento[6] + data_nascimento[7] + data_nascimento[8] + data_nascimento[9] + "/" + data_nascimento[3] + data_nascimento[4] + "/" + data_nascimento[0] + data_nascimento[1]
            
            numero_telefone = int(input("NÚMERO DE TELEFONE: "))
            
            insert_data(cpf, nome_completo, sexo, data_nascimento, numero_telefone)
            
            resposta = str(input("CONTINUAR A CADASTRAR CLIENTE? ")).upper()
            
            while resposta != "SIM" and resposta != "NÃO":
                print("\nRESPONDA APENAS: 'SIM' OU 'NÃO'\n")
                resposta = str(input("CONTINUAR A CADASTRAR CLIENTE? ")).upper()
                            
            if resposta == "NÃO":
                break
            
    #READ

    elif opcao == 2:
        while True:
            print("\nLISTA DE CLIENTES\n")
            
            read_data()
            
            print()
            
            resposta = str(input("VOLTAR PARA O MENU PRINCIPAL? ")).upper()
            
            while resposta != "SIM" and resposta != "NÃO":
                print("\nRESPONDA APENAS 'SIM' OU 'NÃO'\n")
                resposta = str(input("VOLTAR PARA O MENU PRINCIPAL? ")).upper()
                            
            if resposta == "SIM":
                break
            
    #UPDATE       
        
    elif opcao == 3:
        
        while True:
            print("\nATUALIZAÇÃO DE CLIENTES\n")       
            
            print("AVISO: VOCÊ SÓ PODE ALTERAR SEU NÚMERO DE TELEFONE\n")
            
            cpf = str(input("CPF (XXX.XXX.XXX-XX): "))
            
            cpf = verifica_cpf(opcao, cpf)

            print()
            
            novo_numero_telefone = input(str("NOVO NÚMERO DE TELEFONE: "))
            novo_numero_telefone = int(novo_numero_telefone)
            
            update_data(cpf, novo_numero_telefone)
            
            resposta = str(input("VOLTAR PARA O MENU PRINCIPAl? ")).upper()
            
            while resposta != "SIM" and resposta != "NÃO":
                print("\nRESPONDA APENAS 'SIM' OU 'NÃO'\n")
                resposta = str(input("VOLTAR PARA O MENU PRINCIPAl? ")).upper()
                                            
            if resposta == "SIM":
                break
            
    #DELETE
        
    elif opcao == 4:
        while True:
            print("\nDELETAÇÃO DE CLIENTES\n")
            
            cpf = str(input("CPF (XXX.XXX.XXX-XX): "))
            
            cpf = verifica_cpf(opcao, cpf)
            
            delete_data(cpf)
            
            resposta = str(input("CONTINUAR A DELETAR CLIENTE? ")).upper()
            
            while resposta != "SIM" and resposta != "NÃO":
                print("\nRESPONDA APENAS: 'SIM' OU 'NÃO'\n")
                resposta = str(input("CONTINUAR A DELETAR CLIENTE? ")).upper()
                            
            if resposta == "NÃO":
                break
            
    #OUT    
        
    elif opcao == 5:
        print("\nSISTEMA ENCERRADO COM SUCESSO\n")
        break
