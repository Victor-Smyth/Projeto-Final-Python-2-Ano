import mysql.connector


def conectar():
   return mysql.connector.connect(host="localhost", user="root", password="", database="dados")


def inserir_registro():
   try:
       nome = input("Digite o nome: ")
       email = input("Digite o email: ")
       senha = input("Digite a senha: ")


       mysqldb = conectar()
       cursor = mysqldb.cursor()


       cursor.execute("INSERT INTO usuarios(nome, email, senha) VALUES (%s, %s, %s)", (nome, email, senha))
       mysqldb.commit()
       print("Registro inserido com sucesso!")


   except Exception as e:
       print("Erro ao inserir registro:", e)


   finally:
       mysqldb.close()


def exibir_registros():
   try:
       mysqldb = conectar()
       cursor = mysqldb.cursor()


       cursor.execute("SELECT * FROM usuarios")
       registros = cursor.fetchall()


       for registro in registros:
           print(registro)


   except Exception as e:
       print("Erro ao exibir registros:", e)


   finally:
       mysqldb.close()


def atualizar_registro():
   try:
       id_registro = int(input("Digite o ID do registro que deseja atualizar: "))
       novo_nome = input("Digite o novo nome: ")
       novo_email = input("Digite o novo email: ")
       nova_senha = input("Digite a nova senha: ")


       mysqldb = conectar()
       cursor = mysqldb.cursor()


       cursor.execute("UPDATE usuarios SET nome=%s, email=%s, senha=%s WHERE id=%s",
                      (novo_nome, novo_email, nova_senha, id_registro))
       mysqldb.commit()
       print("Registro atualizado com sucesso!")


   except Exception as e:
       print("Erro ao atualizar registro:", e)


   finally:
       mysqldb.close()


def excluir_registro():
   try:
       id_registro = int(input("Digite o ID do registro que deseja excluir: "))


       mysqldb = conectar()
       cursor = mysqldb.cursor()


       cursor.execute("DELETE FROM usuarios WHERE id=%s", (id_registro,))
       mysqldb.commit()
       print("Registro excluído com sucesso!")


   except Exception as e:
       print("Erro ao excluir registro:", e)


   finally:
       mysqldb.close()


# Menu principal
while True:
   print("\nEscolha uma operação:")
   print("1. Inserir Registro")
   print("2. Exibir Registros")
   print("3. Atualizar Registro")
   print("4. Excluir Registro")
   print("5. Sair")


   escolha = input("Digite o número da operação desejada: ")


   if escolha == "1":
       inserir_registro()
   elif escolha == "2":
       exibir_registros()
   elif escolha == "3":
       atualizar_registro()
   elif escolha == "4":
       excluir_registro()
   elif escolha == "5":
       print("Saindo do programa. Até mais!")
       break
   else:
       print("Opção inválida. Tente novamente.")