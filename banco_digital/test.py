# test.py
# Exemplo simples para testar @property, getter/setter em atributos protegidos e privados

class Conta:
    def __init__(self, owner: str, balance: float = 0.0):
        self.__owner = owner     # atributo "privado" (name mangling)
        self._balance = float(balance)  # atributo "protegido" (convenção)

    # owner é exposto como propriedade somente leitura (getter)
    @property
    def owner(self) -> str:
        return self.__owner

    # balance com getter e setter (validação no setter)
    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, value: float):
        if value < 0:
            raise ValueError("Saldo não pode ser negativo")
        self._balance = float(value)

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Valor de depósito deve ser positivo")
        self._balance += amount

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Valor de saque deve ser positivo")
        if amount > self._balance:
            raise ValueError("Saldo insuficiente")
        self._balance -= amount


if __name__ == "__main__":
    c = Conta("Alice", 100.0)

    print("Owner (propriedade read-only):", c.owner)
    print("Balance (via property):", c.balance)

    # Usando métodos que alteram _balance
    c.deposit(50)
    print("Após depósito de 50:", c.balance)

    # Usando setter da propriedade balance com validação
    c.balance = 120.0
    print("Após atribuir balance = 120:", c.balance)

    # Tentativa de atribuir saldo negativo -> erro
    try:
        c.balance = -10
    except ValueError as e:
        print("Erro ao setar balance negativo:", e)

    # Acesso direto ao atributo protegido (convenção, não imposto)
    c._balance = 999.0
    print("Acesso direto a _balance (protegido):", c._balance, "=> property balance:", c.balance)

    # Atributo privado é acessível via name mangling (não recomendado)
    print("Atributo privado (name mangling):", c._Conta__owner)

    # Tentativa de alterar owner via atribuição direta falha (propriedade read-only)
    try:
        c.owner = "Bob"
    except AttributeError as e:
        print("Erro ao tentar setar owner diretamente:", e)