"""
Módulo de histórico bancário.

Fornece a classe Historico que registra eventos (abertura, depósito, saque, transferência)
com timestamp usando datetime. Cada entrada é um dicionário em memória; a classe expõe
métodos para registrar e recuperar entradas.

Exemplo de uso:
	h = Historico()
	h.registrar("Abertura", 100.0, "Conta aberta")
	print(h)
"""

from datetime import datetime
from typing import List, Dict, Optional


class Historico:
	def __init__(self) -> None:
		self._entradas: List[Dict] = []

	def registrar(self, tipo: str, valor: float = 0.0, descricao: str = "", origem: Optional[int] = None, destino: Optional[int] = None) -> None:
		"""Registra um evento no histórico com timestamp.

		Args:
			tipo: Tipo do evento (ex: 'Depósito', 'Saque', 'Transferência').
			valor: Valor associado ao evento.
			descricao: Texto descritivo opcional.
			origem: Conta origem (número) para transferências de entrada.
			destino: Conta destino (número) para transferências de saída.
		"""
		agora = datetime.now()
		entrada = {
			"timestamp": agora,
			"tipo": tipo,
			"valor": float(valor),
			"descricao": descricao,
			"origem": origem,
			"destino": destino,
		}
		self._entradas.append(entrada)

	def entradas(self) -> List[Dict]:
		"""Retorna uma cópia da lista de entradas do histórico."""
		return list(self._entradas)

	def __str__(self) -> str:
		linhas: List[str] = []
		for e in self._entradas:
			ts = e["timestamp"].strftime("%Y-%m-%d %H:%M:%S")
			tipo = e["tipo"]
			valor = f"{e['valor']:.2f}"
			descricao = (" - " + e["descricao"]) if e["descricao"] else ""
			origem = f" de {e['origem']}" if e["origem"] else ""
			destino = f" para {e['destino']}" if e["destino"] else ""
			linhas.append(f"[{ts}] {tipo}{origem}{destino}: R$ {valor}{descricao}")
		return "\n".join(linhas)

