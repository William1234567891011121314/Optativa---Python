import random
class Pessoa:
    def __init__(self, nome, idade, endereco, cpf, sexo):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cpf = cpf
        self.sexo = sexo
    def resumo(self):
        print(f"Nome: {self.nome}\nIdade: {self.idade}\nEndereço: {self.endereco}\nCPF: {self.cpf}\nSexo: {self.sexo}")

class Pai:
    def __init__(self, filhos, esposa, nome, idade, endereco, cpf, sexo):
        super().__init__(self, nome, idade, endereco, cpf, sexo)
        self.filhos = filhos
        self.esposa = esposa
    def resumo(self):
        print(f"Nome: {self.nome}\nIdade: {self.idade}\nEndereço: {self.endereco}\nCPF: {self.cpf}\nSexo: {self.sexo}\nFilhos: {self.filhos}\nEsposa: {self.esposa}")
    def fazerFilho(self, filho):
        self.filhos.append(filho)
        

class Mae:
    def __init__(self, filhos, esposo, nome, idade, endereco, cpf, sexo):
        super.__init__(self, nome, idade, endereco, cpf, sexo)
        self.filhos = filhos
        self.esposo = esposo
    def resumo(self):
        print(f"Nome: {self.nome}\nIdade: {self.idade}\nEndereço: {self.endereco}\nCPF: {self.cpf}\nSexo: {self.sexo}\nFilhos: {self.filhos}\nEsposo: {self.esposo}")
    def fazerFilho(self, filho):
        self.filhos.append(filho)

class Filho:
    def __init__(self, pai, mae, nome, idade, endereco, cpf, sexo):
        super.__init__(self, nome, idade, endereco, cpf, sexo)
        self.pais = [pai]
        self.maes = [mae]
    def addPai(self, pai):
        self.pais.append(pai)
    def addMae(self, mae):
        self.maes.append(mae)
    def resumo(self):
        print(f"Nome: {self.nome}\nIdade: {self.idade}\nEndereço: {self.endereco}\nCPF: {self.cpf}\nSexo: {self.sexo}\nMaes: {self.maes}\nPais: {self.pais}")


pessoas = []
while True:
    opc = int(input("Digite a opção desejada:\n1 - Fazer uma pessoa.\n2 - Modificar uma pessoa.\n3 - Imprimir pessoas.\n"))
    if opc == 1:
        opc = int(input("Digite o tipo de pessoa a ser adicionada:\n1 - Mae.\n2 - Pai.\n3 - Filho.\n"))
        nome = input("Digite o nome da pessoa: ")
        idade = int(input("Digite a idade da pessoa: "))
        endereco = input("Digite o endereco da pessoa: ")
        cpf = input("Digite o cpf da pessoa: ")
        #conjuge

        if opc == 1:
            opc = int(input("Você deseja adicionar um marido a esta pessoa?\n1 - Sim\n2 - Não"))
            if opc == 1:
                while True: #parei aqui
                    searchMarido = input("Digite o nome do marido: ")
                    founded = False
                    for x in range(0, len(pessoas)):
                        if pessoas[x].nome == searchMarido:
                            conjuge = pessoas[x]
                            founded = True
            pessoa = Mae(nome, idade, endereco, cpf)
        elif opc == 2:
            pessoa = Pai(nome, idade, endereco, cpf)
        else:
            pessoa = Filho(nome, idade, endereco, cpf)
        pessoas.append(pessoa)
    elif opc == 2:
        pessoaNome = input("Digite o nome da pessoa a ser modificada: ")
        founded = False
        for x in range(0, len(pessoas)):
            if pessoas[x].nome == pessoaNome:
                founded = True
                opc = int(input("Digite a informação a ser modificada:\n1 - Nome.\n2 - Idade.\n3 - Endereço.\n4 - CPF.\n5 - Sexo\n6 - Pai (se houver).\n7 - Mãe (se houver).\n8 - Filhos (se houver).\n"))
                newInfo = input("Digite a nova informação: ")
                match (opc):
                    case 1:
                        pessoas[x].nome = newInfo
                        break
                    case 2:
                        pessoas[x].idade = newInfo
                        break
                    case 3:
                        pessoas[x].endereco = newInfo
                        break
                    case 4:
                        pessoas[x].cpf = newInfo
                        break
                    case 5:
                        pessoas[x].sexo = newInfo
                        break
                    case 6:
                        if pessoas[x].__class__.__name__ == "Filho":
                            pessoas[x].pai = newInfo
                        else:
                            print("Esta pessoa não pode ter pai pois não é do tipo filho!")
                        break
                    case 7:
                        if pessoas[x].__class__.__name__ == "Filho":
                            pessoas[x].mae = newInfo
                        else:
                            print("Esta pessoa não pode ter mãe pois não é do tipo filho!")
                        break
                    case 8:
                        if pessoas[x].__class__.__name__ == "Mae" or pessoas[x].__class__.__name__ == "Pai":
                            opc = int(input("Digite a ação desejada:\n1 - Adicionar filho.\n2 - Remover filho.\n"))
                            if opc == 1:
                                opc = int(input("Digite o tipo de pessoa a ser adicionada:\n1 - Mae.\n2 - Pai.\n3 - Filho.\n"))
                                nome = input("Digite o nome da pessoa: ")
                                idade = input("Digite a idade da pessoa: ")
                                endereco = input("Digite o endereco da pessoa: ")
                                cpf = input("Digite o cpf da pessoa: ")
                                sexNum = random.randint(1,2)
                                if sexNum == 1:
                                    sexo = "Feminino"
                                else:
                                    sexo = "Masculino"
                                pai
                                mae
                                if pessoas[x].__class__.__name__ == "Mae":
                                    mae = pessoas[x]
                                    while True:
                                        founded = False
                                        searchMarido = input("Digite o nome do marido: ")
                                        for y in range(0, len(pessoas)):
                                            if pessoas[y].nome == searchMarido and pessoas[y].sexo == "Masculino":
                                                pai = pessoas[y]
                                                founded = True
                                        if founded:
                                            break
                                        print("\nPessoa não encontrada!\n")
                                else:
                                    pai = pessoas[x]
                                    while True:
                                        founded = False
                                        searchMarido = input("Digite o nome da esposa: ")
                                        for y in range(0, len(pessoas)):
                                            if pessoas[y].nome == searchMarido and pessoas[y].sexo == "Feminino":
                                                mae = pessoas[y]
                                                founded = True
                                        if founded:
                                            break
                                        print("\nPessoa não encontrada!\n")
                                pessoa = Filho(pai, mae, nome, idade, endereco, cpf, sexo)
                                pessoas[x].fazerFilho(pessoa)
                            else:
                                searchFilho = input("Digite o nome do filho a ser removido: ")
                                founded = False
                                while True:
                                    for y in range(0, len(pessoas)):
                                        if searchFilho == pessoas[y].nome:
                                            pessoas.remove(pessoas[y])
                                            founded = True
                                    if not founded:
                                        print("Esta pessoa não foi encontrada!")
                                    else:
                                        break
    else:
        for x in range(0, len(pessoas)):
            pessoas[x].resumo()