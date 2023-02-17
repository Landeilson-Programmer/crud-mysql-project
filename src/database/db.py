from database.db_connection import *

def read_table():
    cursor.execute("describe Clientes")
    describe_table = cursor.fetchall()
    print(describe_table)
    
def insert_data(cpf, nome_completo, sexo, data_nascimento, numero_telefone):        
    insert = f"INSERT INTO Clientes VALUES ('{cpf}', '{nome_completo}', '{sexo}',' {data_nascimento}', {numero_telefone})"
    cursor.execute(insert)
    conexao.commit()
    print("\nCLIENTE CADASTRADO COM SUCESSO!\n")
    
def read_data():
    read = "SELECT * FROM Clientes"
    cursor.execute(read)
    clientes = cursor.fetchall()
    
    if len(clientes) == 0:
        print("\nNENHUM CLIENTE CADASTRADO\n")
        
    else:
        for cliente in clientes:
            print(cliente) 
    
def update_data(cpf, novo_numero_telefone):
    update = f"UPDATE Clientes SET numero_telefone = {novo_numero_telefone} WHERE cpf = '{cpf}'"       
    cursor.execute(update)
    conexao.commit()
    
    print("\nNÚMERO DE TELEFONE ATUALIZADO COM SUCESSO!\n")
    
def delete_data(cpf):
    delete = f"DELETE FROM Clientes WHERE cpf = '{cpf}'"
    cursor.execute(delete)
    conexao.commit()
    
    print("\nCLIENTE DELETADO COM SUCESSO!\n")
