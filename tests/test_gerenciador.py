from src.gerenciador_tarefas import GerenciadorTarefas
from src.gerenciador_tarefas import Tarefa

def test_cirar_tarefa():
    tarefa = Tarefa("Tarefa 1", "Ir para a academia")
    assert tarefa.titulo == "Tarefa 1"
    assert tarefa.concluida == False
    assert tarefa.descricao == "Ir para a academia"

def test_marcar_tarefa():
    tarefa = Tarefa("Tarefa 1", "Ir ao mercado")
    tarefa.marcar_concluida()
    assert tarefa.concluida == True

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
    assert [repr(t) for t in g.listar_tarefas_pendentes()] == [
        '❌ Tarefa 1', '❌ Tarefa 2', '❌ Tarefa 3'
    ]


def test_listar_tarefas_concluidas():
    g = GerenciadorTarefas()
    t1 = g.adicionar_tarefa("Tarefa 1", "Ir ao mercado")
    t2 = g.adicionar_tarefa("Tarefa 2", "Comprar pão")
    t3 = g.adicionar_tarefa("Tarefa 3", "Comprar queijo")
    g.adicionar_tarefa("Tarefa 4", "Comprar carne")
    t1.marcar_concluida()
    t2.marcar_concluida()
    t3.marcar_concluida()
    assert [repr(t) for t in g.listar_tarefas_concluidas()] == [
        '✅ Tarefa 1', '✅ Tarefa 2', '✅ Tarefa 3'
    ]


def test_marcar_tarefa_concluida():
    g = GerenciadorTarefas()
    g.adicionar_tarefa("Tarefa 1", "Ir ao mercado")
    g.adicionar_tarefa("Tarefa 2", "Comprar pão")
    g.adicionar_tarefa("Tarefa 3", "Comprar queijo")
    t1 = g.marcar_tarefa_concluida("Tarefa 1")
    t2 = g.marcar_tarefa_concluida("Tarefa 2")
    t3 = g.marcar_tarefa_concluida("Tarefa 3")
    assert all([t1.concluida & t2.concluida & t3.concluida])

def test_marcar_tarefa_inexistente():
    g = GerenciadorTarefas()
    g.adicionar_tarefa("Tarefa 1", "Ir ao mercado")
    g.adicionar_tarefa("Tarefa 2", "Comprar pão")
    g.adicionar_tarefa("Tarefa 3", "Comprar queijo")
    assert g.marcar_tarefa_concluida("Jogar futebol") == None
