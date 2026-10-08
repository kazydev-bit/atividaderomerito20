from sqlalchemy import select

from models import Livro


def emprestar_livro(session, titulo):
    livro = session.scalar(
        select(Livro).where(Livro.titulo == titulo)
    )

    if livro is None:
        print("Livro não encontrado.")
        return

    if not livro.disponivel:
        print("Livro já está emprestado.")
        return

    livro.disponivel = False
    session.commit()

    print("Livro emprestado.")


def devolver_livro(session, titulo):
    livro = session.scalar(
        select(Livro).where(Livro.titulo == titulo)
    )

    if livro is None:
        print("Livro não encontrado.")
        return

    livro.disponivel = True
    session.commit()

    print("Livro devolvido.")