from flask import Flask, render_template, request, redirect, url_for
from models.database import init_db
from models.tarefa import Tarefa

app = Flask(__name__)

init_db()

@app.route('/')
def home():
    return render_template('home.html', titulo='Home')

@app.route('/lista', methods=['GET', 'POST'])
def agenda():
    tarefas = None

    if request.method == 'POST':
        titulo_tarefa = request.form['titulo-tarefa']
        data_conclusao = request.form['data-conclusao']
        tipo = request.form['tipo']

        tarefa = Tarefa(titulo_tarefa, data_conclusao, tipo)
        tarefa.salvar_tarefa()

        return redirect(url_for('agenda'))

    tarefas = Tarefa.obter_tarefas()
    return render_template('lista.html', titulo='Agenda de Lazer', tarefas=tarefas)

@app.route('/delete/<int:idTarefa>')
def delete(idTarefa):
    tarefa = Tarefa.id(idTarefa)
    tarefa.excluir_tarefa()
    return redirect(url_for('agenda'))

@app.route('/update/<int:idTarefa>', methods=['GET', 'POST'])
def update(idTarefa):
    if request.method == 'POST':
        titulo = request.form['titulo-tarefa']
        data = request.form['data-conclusao']
        tipo = request.form['tipo']
        tarefa = Tarefa(titulo, data, tipo, idTarefa)
        tarefa.atualizar_tarefa()
        return redirect(url_for('agenda'))

    tarefas = Tarefa.obter_tarefas()
    tarefa_selecionada = Tarefa.id(idTarefa)
    return render_template('lista.html', titulo=f'Editando a tarefa ID: {idTarefa}', tarefas=tarefas, tarefa_selecionada=tarefa_selecionada)

@app.route("/toggle/<int:id>", methods=["POST"])
def toggle(id):
    tarefa = Tarefa.id(id)
    tarefa.toggle_conclusao()

    return ("", 204)