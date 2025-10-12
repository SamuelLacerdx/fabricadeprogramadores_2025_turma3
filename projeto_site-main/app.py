from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Funções para manipular arquivos
def salvar_em_arquivo(arquivo, texto):
    with open(arquivo, 'a') as f:
        f.write(texto + '\n')

def ler_arquivo(arquivo):
    try:
        with open(arquivo, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        return []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adicionar', methods=['POST'])
def adicionar():
    tipo = request.form['tipo']
    valor = request.form['valor']
    descricao = request.form['descricao']

    if tipo == 'ganho':
        salvar_em_arquivo('ganho.txt', f"Ganho: {valor}")
        salvar_em_arquivo('descr_ganho.txt', f"Descrição: {descricao}")
    else:
        salvar_em_arquivo('despesa.txt', f"Despesa: {valor}")
        salvar_em_arquivo('descr_despesa.txt', f"Descrição: {descricao}")

    return redirect(url_for('index'))

@app.route('/extrato')
def extrato():
    ganhos = ler_arquivo('ganho.txt')
    despesas = ler_arquivo('despesa.txt')
    return render_template('extrato.html', ganhos=ganhos, despesas=despesas)

@app.route('/saldo')
def saldo():
    ganhos = ler_arquivo('ganho.txt')
    despesas = ler_arquivo('despesa.txt')

    total_ganhos = sum(float(x.strip().split(': ')[1]) for x in ganhos if x.strip())
    total_despesas = sum(float(x.strip().split(': ')[1]) for x in despesas if x.strip())
    montante = total_ganhos - total_despesas

    return render_template('saldo.html', saldo=montante)

if __name__ == '__main__':
    app.run(debug=True)
