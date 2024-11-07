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