#Funções
def salvar_contatos(lista):
    arquivo = open("contatos.txt","w")

    for contato in lista:

        arquivo.write("{}#{}#{}\n".format(contato["nome"], contato["email"],contato["telefone"]))
    arquivo.close()

def carregar_contatos():
    lista = []
    try:

        arquivo = open("contatos.txt", "r")

        for linha in arquivo.readlines():
            coluna = linha.strip().split("#") #quebrar espaços em branco
            contato = {
                "email": coluna [1],
                "nome": coluna[0],
                "telefone":coluna[2]
            }
            lista.append(contato)
        arquivo.close()
    except FileNotFoundError:
        pass

    return lista



def existe_contato(lista, email):
    if len(lista) > 0:
      for contato in lista:
        if contato ["email"] == email:
         return True

    return False

def adicionar(lista):

    while True:
         email = input("Digite o e-mail do contato:")

         if not existe_contato(lista, email):
            break
         else:
            print("Esse email ja foi utilizado. Por favor tente um novo email")

        #nesse passo o email recebido será unico

    contato = {
        "email" : email,
        "nome": input("Digite o nome:"),
        "telefone": input(("Digite o telefone"))
}
    lista.append(contato)

    print("O contato {} foi cadastrado com sucesso!\n".format(contato['nome']))

def alterar(lista):
    print("==Alterar contato==")
    if len(lista) > 0:
        email = input("Digite o email do contato")
        if existe_contato(lista, email):
            for contato in lista:
                if contato['email'] == email:
                    print(" Nome:{}".format(contato['nome']))
                    print("Email:{}".format(contato['email']))
                    print("Telefone:{}".format(contato['telefone']))
                    print("=============================================")

                    contato['nome'] = input ("Digite o novo nome: ")
                    contato['telefone'] = input("Digite o novo telefone do contato: ")

                    print("Contato alterado com sucesso!")
                    break
        else:
            print("Não existe nem um contato com o email {}".format(email))
    else:
        print("Não existe nem um contato cadastrado\n")

def excluir(lista):
    print("==Excluir contato==")
    if len(lista) > 0:
        email = input("Digite o email do contato para excluir: ")
        if existe_contato(lista, email):
            print("O contato foi encontrado. As informações seguem abaixo: ")
            for i, contato in enumerate(lista):
                if contato['email'] == email:
                    print(" Nome:{}".format(contato['nome']))
                    print("Email:{}".format(contato['email']))
                    print("Telefone:{}".format(contato['telefone']))
                    print("=============================================")

                    del lista[i]

                    print("Contato excluido com sucesso!")
                    break
        else:
            print("Não existe nem um contato cadastrado com esse email{}\n".format(email))
    else:
        print("Não existe contato cadastrado \n")

def buscar(lista):
    print("==Buscar contato==")
    if len(lista) > 0:
        email = input("Digite o email do contato")
        if existe_contato(lista , email):
            for contato in lista:
                if contato ['email'] == email:
                    print(" Nome:{}".format(contato["nome"]))
                    print("Email:{}".format(contato["email"]))
                    print("Telefone:{}".format(contato["telefone"]))
                    print("=============================================")
                    break
        else:
            print("Não existe nem um contato com o email {}".format(email))


        print("Quantidade de contatos: {}\n".format(len(lista)))
    else:
        print("Não existe nem um contato cadastrado\n")

def listar( lista):
    print("==Listar contatos==")
    if len (lista) > 0:
        for i,contato in enumerate(lista):
            print("contato{}:".format(i+1))
            print("\t Nome:{}".format(contato["nome"]))
            print("\tEmail:{}".format(contato["email"]))
            print("\t Telefone:{}".format(contato["telefone"]))
            print("=============================================")

        print("Quantidade de contatos: {}\n".format(len(lista)))
    else:("Não existe nem um contato cadastrado\n")
#Função principal
def principal ():
    lista = carregar_contatos() #inicializando a lista de contatos
    while True:
            print(" ===Agenda de contatos===")
            print(" 1- Adicionar contato")
            print(" 2- Alterar contato")
            print(" 3- Exluir contato ")
            print(" 4- Buscar contato")
            print(" 5- Listar contatos")
            print(" 6- Sair")
            opção = int(input("> "))

            if opção == 1:
                adicionar(lista)
                salvar_contatos(lista)
            elif opção == 2:
                alterar(lista)
                salvar_contatos(lista)
            elif opção == 3:
                excluir(lista)
                salvar_contatos(lista)
            elif opção == 4:
                buscar(lista)
            elif opção == 5:
                listar( lista)
            elif opção == 6:
                print("saindo do programa...")
                break
            else: print("Opção inválida. Por favor, tente novamente.")

principal ()