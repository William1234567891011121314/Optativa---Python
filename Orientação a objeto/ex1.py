class carro:
    ligado = False
    andando = False
    def ligarMotor(self):
        self.ligado = True
        self.printarStatus()
    def desligarMotor(self):
        self.ligado = False
        self.printarStatus()
    def andar(self):
        if self.ligado:
            self.andando = True
        self.printarStatus()
    def parar(self):
        self.andando = False
        self.printarStatus()
    def printarStatus(self):
        print(f"\nLigado: {self.ligado}\nAndando: {self.andando}")

carro = carro()
while True:
    opc = int(input("\nO que você deseja?\n1 - Ligar o carro\n2 - Desligar o carro\n3 - Andar\n4 - Parar\n5 - Sair do carro\n"))
    match(opc):
        case 1:
            carro.ligarMotor()
        case 2:
            carro.desligarMotor()
        case 3:
            carro.andar()
        case 4:
            carro.parar()
        case 5:
            break
        case _:
            print("Não existe essa opção!\n")