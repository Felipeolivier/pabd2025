import sys
from typing import Optional

try:
    # quando importado como pacote
    from .history_bank import Historico
except Exception:
    try:
        # quando executado diretamente no diretório banco_digital
        from history_bank import Historico
    except Exception:
        # fallback quando o pacote estiver instalado/importável
        from banco_digital.history_bank import Historico

class Conta:

    def __init__(self, Titular: str, CPF: str, account: int, Agencia: int, Saldo: float = 0.0, Email: str = ""):
        if not isinstance(Titular, str) or not Titular:
            raise ValueError("titular deve ser uma string não vazia")
        if not isinstance(CPF, str) or not CPF:
            raise ValueError("CPF deve ser uma string não vazia")
        if not isinstance(account, int) :
            raise ValueError("conta deve ser um inteiro")
        if not isinstance(Saldo, (int, float)):
            raise ValueError("saldo deve ser um número")
        if not isinstance(Email, str):
            raise ValueError("email deve ser uma string")
        if not isinstance(Agencia, int):
            raise ValueError("agencia deve ser um inteiro")
        
        self.titular = Titular
        self.account = account
        self.agencia = Agencia
        self.saldo = float(Saldo)
        self.email = Email  
        self.historico = Historico()
        # registrar abertura
        self.historico.registrar("Abertura", self.saldo, f"Abertura da conta com saldo inicial: {self.saldo:.2f}")

    def depositar(self, valor: float, descricao: str = "") -> None:
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("valor de depósito deve ser número positivo")
        self.saldo += float(valor)
        self.historico.registrar("Depósito", valor, descricao)

    def sacar(self, valor: float, descricao: str = "") -> None:
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("valor de saque deve ser número positivo")
        if float(valor) > self.saldo:
            raise ValueError("saldo insuficiente")
        self.saldo -= float(valor)
        self.historico.registrar("Saque", valor, descricao)

    def transferir(self, destino: 'Conta', valor: float, descricao: str = "") -> None:
        if not isinstance(destino, Conta):
            raise ValueError("destino deve ser uma instancia de Conta")
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("valor de transferência deve ser número positivo")
        if float(valor) > self.saldo:
            raise ValueError("saldo insuficiente para transferência")
        # debitar origem
        self.saldo -= float(valor)
        self.historico.registrar("Transferência (saida)", valor, descricao, origem=self.account, destino=destino.account)
        # creditar destino
        destino.saldo += float(valor)
        destino.historico.registrar("Transferência (entrada)", valor, descricao, origem=self.account, destino=destino.account)

    def __repr__(self) -> str:
        return f"Conta(titular={self.titular!r}, conta={self.account}, agencia={self.agencia}, saldo=R$ {self.saldo:.2f})"


if __name__ == "__main__":
    # Teste rápido
    conta1 = Conta(
        Titular="Maria Oliveira",
        CPF="98765432100", 
        account=2939982932,
        Agencia=1001,
        Saldo=2552.50, 
        Email="" )

    conta2 = Conta(
        Titular="João Silva",
        CPF="12345678900", 
        account=1002003004,
        Agencia=1001,
        Saldo=500.00, 
        Email="joao@example.com" )

    print(conta1)
    conta1.depositar(200.0, "Depósito via caixa")
    conta1.sacar(100.0, "Saque ATM")
    conta1.transferir(conta2, 300.0, "Pagamento")

    print("\n--- Histórico conta1 ---")
    print(conta1.historico)
    print("\n--- Histórico conta2 ---")
    print(conta2.historico)