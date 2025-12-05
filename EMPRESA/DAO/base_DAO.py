# EMPRESA/DAO/base_DAO.py  
# Módulo: base_DAO.py — Classe base para DAOs com operações CRUD (data access object)

from abc import ABC, abstractmethod
from typing import List, Optional, Any
from typing import TypeVar, Generic
from supabase import Client
from dataclasses import asdict
from EMPRESA.models.funcionary import Funcionario



from supabase import Client

# Definindo um tipo genérico T para representar o tipo de entidade que o DAO irá manipular
#tornar uma classe generica
T = TypeVar('T')

class BaseDAO(ABC, Generic[T]):
    """Classe base abstrata para DAOs com operações CRUD."""
    
    def __init__(self, supabase_client: Client, table_name: str):
        self._client= supabase_client
        self._table_name = table_name



# dict --> model / model --> dict
#''' as instancias abaixo permitem qualquer classe criar as suas proprias conversoes do modelo para dict e vice versa'''

    @abstractmethod
    def to_model(self, data: dict) -> T:
        """Converte um dicionário em uma instância do modelo."""
        pass

    @abstractmethod
    def to_dict(self, model: T) -> dict:
        """Converte uma instância do modelo em um dicionário."""
        pass

    #create 
    @abstractmethod
    def create(self, model: T) -> Any:
        """Cria uma nova entidade no banco de dados."""
        try :
            data = self.to_dict(model)
            response = self.client.table(self.table_name).insert(data).execute()
            return response.data
        except Exception as e:
            print(f"Erro ao criar entidade: {e}")
            return None

    #read

        #retorna todas as entidades de uma tabela
    def read_all(self) -> List[T]:
        try :
            response = self.client.table(self.table_name).select("*").execute()
            if response.data: 
                return [self.to_model(item) for item in response.data]
            return []
        except Exception as e:
            print(f"Erro ao ler todas as entidades: {e}")
            return []
        

    @abstractmethod
    def read(self, pk: str, value: T) -> Optional[T]:
        """Lê uma entidade do banco de dados pelo ID."""
        try :
            response = self.client.table(self.table_name).select("*").eq(pk, value).execute()
            if response.data and len(response.data) > 0: 
                return [self.to_model(item) for item in response.data]
            return None
        except Exception as e:
            print(f"Erro ao ler todas as entidades: {e}")
            return None


    #update

    def update(self, pk: str, value: T, model: T) -> bool:
        """Atualiza uma entidade no banco de dados."""
        try :
            data = self.to_dict(model)
            response = self.client.table(self.table_name).update(data).eq(pk, value).execute()
            return response.status_code == 200
        except Exception as e:
            print(f"Erro ao atualizar entidade: {e}")
            return False

    #delete

    def delete(self, pk: str, value: T) -> bool:
        """Deleta uma entidade do banco de dados."""
        try :
            response = self.client.table(self.table_name).delete().eq(pk, value).execute()
            return response.status_code == 200
        except Exception as e:
            print(f"Erro ao deletar entidade: {e}")
            return False