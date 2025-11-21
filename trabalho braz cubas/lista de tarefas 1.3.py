import json
import os
#aquivo para armazenar as tarefas
DATA_FILE = "tarefas.json"
#função para carregar as tarefas do arquivo
def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
#função para salvar as tarefas no arquivo
def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)
#função para gerar o próximo ID
def next_id(tasks):
    return max((t["id"] for t in tasks), default=0) + 1
#função para adicionar uma nova tarefa
def add_task(tasks):
    title = input("Título: ").strip()
    if not title:
        print("Título obrigatório.")
        return
    tasks.append({"id": next_id(tasks), "title": title, "done": False})
    save_tasks(tasks)
    print("Tarefa adicionada.")
#função para listar as tarefas
def list_tasks(tasks, only_pending=False):
    shown = [t for t in tasks if not only_pending or not t["done"]]
    if not shown:
        print("Nenhuma tarefa.")
        return
    for t in shown:
        mark = "✓" if t["done"] else " "
        print(f"[{mark}] id:{t['id']} - {t['title']}")
#função para marcar ou desmarcar uma tarefa como feita
def toggle_done(tasks, set_done=True):
    try:
        tid = int(input("ID da tarefa: ").strip())
    except ValueError:
        print("ID inválido.")
        return
    for t in tasks:
        if t["id"] == tid:
            t["done"] = set_done
            save_tasks(tasks)
            print("Atualizado.")
            return
    print("Tarefa não encontrada.")
#função para remover uma tarefa
def remove_task(tasks):
    try:
        tid = int(input("ID da tarefa a remover: ").strip())
    except ValueError:
        print("ID inválido.")
        return
    for t in tasks:
        if t["id"] == tid:
            tasks.remove(t)
            save_tasks(tasks)
            print("Removida.")
            return
    print("Tarefa não encontrada.")
#função principal do programa cada numeração corresponde a uma ação
def main():
    tasks = load_tasks()
    while True:
        print("\n1 Listar todas  2 Listar pendentes  3 Adicionar  4 Marcar feita")
        print("5 Marcar pendente  6 Remover  0 Sair")
        cmd = input("Opção: ").strip()
        if cmd == "1":
            list_tasks(tasks)
        elif cmd == "2":
            list_tasks(tasks, only_pending=True)
        elif cmd == "3":
            add_task(tasks)
        elif cmd == "4":
            toggle_done(tasks, True)
        elif cmd == "5":
            toggle_done(tasks, False)
        elif cmd == "6":
            remove_task(tasks)
        elif cmd == "0":
            save_tasks(tasks)
            print("Saindo.")
            break
        else:
            print("Opção inválida.")
#iniciar o programa
if __name__ == "__main__":
    main()
