import flet as ft
from main import (
    ler_dados,
    atualizar_nota,
    criar_novo_usuario_e_nota,
    deletar_usuario,
    login_de_usuario,
    matricular_aluno,
)
from tabelas import Usuario, Nota


def main(page: ft.Page):
    page.title = "Sistema de Notas"
    page.window_width = 800
    page.window_height = 600

    def exibir_home(e=None):
        page.controls.clear()
        page.controls.append(
            ft.Column([
                ft.Text("Bem-vindo à Home!", size=24, weight="bold"),
                ft.ElevatedButton("Ver Usuários", on_click=mostrar_usuarios),
                ft.ElevatedButton("Cadastrar Usuário e Nota", on_click=exibir_formulario_cadastro),
                ft.ElevatedButton("Login", on_click=exibir_login),
                ft.ElevatedButton("Atualizar Nota", on_click=exibir_formulario_atualizar_nota),
                ft.ElevatedButton("Deletar Usuário", on_click=exibir_formulario_deletar_usuario),
                ft.ElevatedButton("Matricular Aluno", on_click=exibir_formulario_matricula),
            ])
        )
        page.update()

    def mostrar_usuarios(e=None):
        page.controls.clear()
        try:
            dados = ler_dados()
            lista = ft.Column([
                ft.Text("Usuários cadastrados", size=20, weight="bold"),
                *[
                    ft.Text(
                        f"ID: {u['id']}, Nome: {u['usuario']}, Email: {u['email']}, Notas: {len(u['notas'])}"
                    ) for u in dados
                ]
            ])
        except Exception as ex:
            lista = ft.Text(f"Erro ao ler dados: {ex}", color="red")
        page.controls.append(lista)
        page.controls.append(ft.ElevatedButton("Voltar", on_click=exibir_home))
        page.update()

    def exibir_formulario_cadastro(e=None):
        nome = ft.TextField(label="Nome")
        email = ft.TextField(label="Email")
        senha = ft.TextField(label="Senha", password=True)
        titulo = ft.TextField(label="Título da Nota")
        conteudo = ft.TextField(label="Conteúdo da Nota")

        def enviar(e):
            try:
                user = Usuario(nome=nome.value, email=email.value, senha_hash=senha.value)
                note = Nota(titulo=titulo.value, conteudo=conteudo.value)
                criar_novo_usuario_e_nota(user, note)
                page.snack_bar = ft.SnackBar(ft.Text("Usuário e nota criados com sucesso!"), bgcolor="green")
            except Exception as ex:
                page.snack_bar = ft.SnackBar(ft.Text(f"Erro: {ex}"), bgcolor="red")
            page.snack_bar.open = True
            page.update()

        page.controls.clear()
        page.controls.append(
            ft.Column([
                ft.Text("Cadastrar Usuário e Nota", size=20, weight="bold"),
                nome, email, senha, titulo, conteudo,
                ft.Row([
                    ft.ElevatedButton("Cadastrar", on_click=enviar),
                    ft.ElevatedButton("Voltar", on_click=exibir_home),
                ])
            ])
        )
        page.update()

    def exibir_login(e=None):
        email = ft.TextField(label="Email")
        senha = ft.TextField(label="Senha", password=True)

        def logar(e):
            try:
                user = Usuario(email=email.value, senha_hash=senha.value)
                usuario_logado = login_de_usuario(user)
                if usuario_logado:
                    page.snack_bar = ft.SnackBar(
                        ft.Text(f"Login realizado com sucesso! Bem-vindo, {usuario_logado.nome}."),
                        bgcolor="green"
                    )
                else:
                    page.snack_bar = ft.SnackBar(ft.Text("Email ou senha incorretos."), bgcolor="red")
            except Exception as ex:
                page.snack_bar = ft.SnackBar(ft.Text(f"Erro: {ex}"), bgcolor="red")
            page.snack_bar.open = True
            page.update()

        page.controls.clear()
        page.controls.append(
            ft.Column([
                ft.Text("Login de Usuário", size=20, weight="bold"),
                email, senha,
                ft.Row([
                    ft.ElevatedButton("Entrar", on_click=logar),
                    ft.ElevatedButton("Voltar", on_click=exibir_home),
                ])
            ])
        )
        page.update()

    def exibir_formulario_atualizar_nota(e=None):
        id_nota = ft.TextField(label="ID da Nota")
        novo_titulo = ft.TextField(label="Novo Título")
        novo_conteudo = ft.TextField(label="Novo Conteúdo")

        def atualizar(e):
            try:
                atualizar_nota(int(id_nota.value), novo_titulo.value, novo_conteudo.value)
                page.snack_bar = ft.SnackBar(ft.Text("Nota atualizada com sucesso!"), bgcolor="green")
            except Exception as ex:
                page.snack_bar = ft.SnackBar(ft.Text(f"Erro ao atualizar: {ex}"), bgcolor="red")
            page.snack_bar.open = True
            page.update()

        page.controls.clear()
        page.controls.append(
            ft.Column([
                ft.Text("Atualizar Nota", size=20, weight="bold"),
                id_nota, novo_titulo, novo_conteudo,
                ft.Row([
                    ft.ElevatedButton("Atualizar", on_click=atualizar),
                    ft.ElevatedButton("Voltar", on_click=exibir_home),
                ])
            ])
        )
        page.update()

    def exibir_formulario_deletar_usuario(e=None):
        email = ft.TextField(label="Email do Usuário")

        def deletar(e):
            try:
                deletar_usuario(email.value)
                page.snack_bar = ft.SnackBar(ft.Text("Usuário deletado com sucesso."), bgcolor="green")
            except Exception as ex:
                page.snack_bar = ft.SnackBar(ft.Text(f"Erro ao deletar: {ex}"), bgcolor="red")
            page.snack_bar.open = True
            page.update()

        page.controls.clear()
        page.controls.append(
            ft.Column([
                ft.Text("Deletar Usuário", size=20, weight="bold"),
                email,
                ft.Row([
                    ft.ElevatedButton("Deletar", on_click=deletar),
                    ft.ElevatedButton("Voltar", on_click=exibir_home),
                ])
            ])
        )
        page.update()

    def exibir_formulario_matricula(e=None):
        email_usuario = ft.TextField(label="Email do Aluno")
        nome_curso = ft.TextField(label="Nome do Curso")

        def matricular(e):
            try:
                matricular_aluno(email_usuario.value, nome_curso.value)
                page.snack_bar = ft.SnackBar(ft.Text("Aluno matriculado com sucesso!"), bgcolor="green")
            except Exception as ex:
                page.snack_bar = ft.SnackBar(ft.Text(f"Erro na matrícula: {ex}"), bgcolor="red")
            page.snack_bar.open = True
            page.update()

        page.controls.clear()
        page.controls.append(
            ft.Column([
                ft.Text("Matricular Aluno", size=20, weight="bold"),
                email_usuario, nome_curso,
                ft.Row([
                    ft.ElevatedButton("Matricular", on_click=matricular),
                    ft.ElevatedButton("Voltar", on_click=exibir_home),
                ])
            ])
        )
        page.update()

    exibir_home()


ft.app(target=main)
