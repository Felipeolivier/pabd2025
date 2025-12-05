class Conta:
    def __init__(self, cliente, agencia, numero, pix, saldo):
        self.cliente = cliente
        self.agencia = agencia
        self.numero = numero
        self.pix = pix
        self.saldo = saldo
    
    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        if(self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            return True
    
    def extrato(self):
        print(f'Titular: {self.cliente.nome}\nCPF: {self.cliente.cpf}\nAgência: {self.agencia}\nNúmero: {self.numero}\nPIX: {self.pix}\nSaldo: {self.saldo:.2f}\n')

    def transfere(self, destino, valor):
        if(self.saca(valor)):
            destino.deposita(valor)
            return True
        else:
            return False
