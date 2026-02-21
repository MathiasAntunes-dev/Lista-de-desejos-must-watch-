from models.database import Database
from typing import Self, Any, Optional
from sqlite3 import Cursor

class Tarefa:
    """
        Classe para representar uma tarefa, com métodos para salvar, obter, excluir e atualizar tarefas em um banco de dados usando a classe `Database`.
    """
    def __init__(self: Self, titulo_tarefa: Optional[str] = '', data_conclusao: Optional[str] = None, tipo: Optional[str] = None, id_tarefa: Optional[int] = None) -> None:
        self.titulo_tarefa: Optional[str] = titulo_tarefa
        self.data_conclusao: Optional[str] = data_conclusao
        self.tipo: Optional[str] = tipo
        self.id_tarefa: Optional[int] = id_tarefa

    @classmethod
    def id(cls, id: int) -> Self:
        with Database() as db:
            query: str = 'SELECT titulo_tarefa, data_conclusao, tipo FROM tarefas WHERE id = ?;'
            params: tuple = (id,)
            resultado: list[Any] = db.buscar_tudo(query, params)
            [[titulo, data, tipo]] = resultado
            
        return cls(id_tarefa=id, titulo_tarefa=titulo, data_conclusao=data, tipo=tipo)

    def salvar_tarefa(self: Self) -> None:
        with Database() as db:
            query: str = "INSERT INTO tarefas (titulo_tarefa, data_conclusao, tipo) VALUES (?, ?, ?);"
            params: tuple = (self.titulo_tarefa, self.data_conclusao, self.tipo)
            db.executar(query, params)

    @classmethod
    def obter_tarefas(cls) -> list[Self]:
        with Database() as db:
            query: str = 'SELECT titulo_tarefa, data_conclusao, tipo, id FROM tarefas;'
            resultados: list[Any] = db.buscar_tudo(query)
            tarefas: list[Self] = [cls(titulo, data, tipo, id) for titulo, data, tipo, id in resultados]
            return tarefas
        
    def excluir_tarefa(self) -> Cursor:
        with Database() as db:
            query: str = 'DELETE FROM tarefas WHERE id = ?;'
            params: tuple = (self.id_tarefa,)
            resultado: Cursor = db.executar(query, params)
            return resultado
    
    def atualizar_tarefa(self: Self):
        with Database() as db:
            query: str = "UPDATE tarefas SET titulo_tarefa = ?, data_conclusao = ?, tipo = ? WHERE id = ?;"
            params: tuple = (self.titulo_tarefa, self.data_conclusao, self.tipo, self.id_tarefa)
            resultado: Cursor = db.executar(query, params)
            return resultado