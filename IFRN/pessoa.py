class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
        self.__matricula = None  # Atributo privado

    # Getter de matrícula
    def get_matricula(self):
        return self.__matricula

    # Getter e Setter de nome
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        if len(novo_nome) > 0:
            self._nome = novo_nome
        else:
            raise ValueError("Nome não pode ser vazio.")

    # Getter e Setter de idade
    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, nova_idade):
        if nova_idade < 0:
            raise ValueError("Idade não pode ser negativa.")
        if nova_idade > 150:
            raise ValueError("Idade inválida.")
        self._idade = nova_idade