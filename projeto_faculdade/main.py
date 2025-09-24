from tabelas import SessionLocal, Usuario, Nota

db = SessionLocal()

def criar_novo_usuario_e_nota(novo_usuario: Usuario, nova_nota: Nota):

    db.add(novo_usuario)
    db.commit()
    print(f"Usuário '{novo_usuario}.nome' criado com ID: {novo_usuario}")

    nova_nota = Nota(
    titulo = "Minha Primeira Nota com SQLAlchemy",
    contudo = "É muito mais fácil do que escrever SQL na mão!",
    autor = novo_usuario 
    )
    db.add(nova_nota)
    db.commit()

def atualizar_nota(id_nota: int):
    """Exemplo de como ATUALIZAR dados."""

    nota_para_editar = db.query(Nota).filter(Nota.id == id_nota).first()

    if nota_para_editar:
        print(f"Título original: '{nota_para_editar.titulo}'")

        nota_para_editar.titulo = "Lista de anotações ATULIZADA!"

        db.commit()
        print(f"Título novo: '{nota_para_editar.titulo}'")

    else:
        print("Nota com ID %d nçao encontrada." % id_nota)

def ler_dados():
    """Exemplo de como LER dados."""

    users = db.query(Usuario).all()

    if users:
        for nota in users.notas:
            print(f" -Título: {nota.titulo} (ID: {nota.id})")
        return users, nota 
    else:
        print("Usuário(a) não encontrado.")

def deletar_usuario(id_usuario: int):
    usuario_deletado = db.query(Usuario).filter(Usuario.id == id_usuario).first()

    if usuario_deletado:

        db.delete(usuario_deletado)
        db.commit()
        print(f"Usuário: '{usuario_deletado.nome}' removido com sucesso!")

    else:
        print("Usuário com ID %d não encontrada." % id_usuario)