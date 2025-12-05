

from supabase import Client
from EMPRESA.DAO import base_DAO
from Funcionario import funcionario


class funcionaryDAO (base_DAO[funcionario]):
    def __init__(self, client: Client):
        super().__init__(client, 'funcionarios')