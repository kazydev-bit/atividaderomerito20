from models import Autor, Livro


def popular_banco(session):
    autor1 = Autor(
        nome="Machado de Assis",
        pais="Brasil"
    )

    autor2 = Autor(
        nome="J. K. Rowling",
        pais="Inglaterra"
    )

    autor3 = Autor(
        nome="George Orwell",
        pais="Inglaterra"
    )

    session.add(autor1)
    session.add_all([autor2, autor3])

    session.commit()

    livro1 = Livro(
        titulo="Dom Casmurro",
        ano=1899,
        autor=autor1,
        disponivel=True
    )

    livro2 = Livro(
        titulo="Memorias Postumas",
        ano=1881,
        autor=autor1,
        disponivel=False
    )

    livros = [
        Livro(
            titulo="Quincas Borba",
            ano=1891,
            autor=autor1,
            disponivel=True
        ),
        Livro(
            titulo="Harry Potter",
            ano=1997,
            autor=autor2,
            disponivel=True
        ),
        Livro(
            titulo="Harry Potter 2",
            ano=1998,
            autor=autor2,
            disponivel=False
        ),
        Livro(
            titulo="1984",
            ano=1949,
            autor=autor3,
            disponivel=True
        )
    ]

    session.add(livro1)
    session.add(livro2)
    session.add_all(livros)

    session.commit()