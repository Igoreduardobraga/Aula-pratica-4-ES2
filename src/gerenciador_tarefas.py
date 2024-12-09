class Tarefa:
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao
        self.concluida = False

    def marcar_concluida(self):
        self.concluida = True

    def __repr__(self):
        status = "✅" if self.concluida else "❌"
        return f"{status} {self.titulo}"


class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, titulo, descricao):
        tarefa_nova = Tarefa(titulo, descricao)
        self.tarefas.append(tarefa_nova)
        return tarefa_nova

    def listar_tarefas_pendentes(self):
        return [t for t in self.tarefas if not t.concluida]

    def listar_tarefas_concluidas(self):
        return [t for t in self.tarefas if t.concluida]

    def marcar_tarefa_concluida(self, titulo):
        for tarefa in self.tarefas:
            if tarefa.titulo == titulo:
                tarefa.marcar_concluida()
                return tarefa
        return None
