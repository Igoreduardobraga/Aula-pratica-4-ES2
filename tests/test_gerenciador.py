import pytest
from src.gerenciador_tarefas import GerenciadorTarefas


def test_adicionar_tarefa():
    g = GerenciadorTarefas()
    t = g.adicionar_tarefa("Tarefa 1", "Ir ao mercado")
    assert t.titulo == "Tarefa 1"
    assert t.descricao == "Ir ao mercado"
    assert t.concluida == False
    assert len(g.tarefas) == 1


def test_listar_tarefas_pendentes():
    g = GerenciadorTarefas()
    g.adicionar_tarefa("Tarefa 1", "Ir ao mercado")
    g.adicionar_tarefa("Tarefa 2", "Comprar pão")
    g.adicionar_tarefa("Tarefa 3", "Comprar queijo")
    assert [repr(t) for t in g.tarefas] == ['❌ Tarefa 1', '❌ Tarefa 2', '❌ Tarefa 3']
    assert len(g.tarefas) == 3
