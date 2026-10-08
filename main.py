from consultas import (
    buscar_livros_por_titulo,
    listar_livros,
    listar_livros_disponiveis,
    listar_livros_por_autor,
)

from database import criar_banco, nova_sessao

from operacoes import devolver_livro, emprestar_livro

from seed import popular_banco


criar_banco()

with nova_sessao() as session:
    popular_banco(session)

    print("\nTodos os livros:")
    listar_livros(session)

    print("\nLivros disponíveis:")
    listar_livros_disponiveis(session)

    print("\nBusca por título:")
    buscar_livros_por_titulo(session, "Harry")

    print("\nLivros de Machado:")
    listar_livros_por_autor(session, "Machado de Assis")

    print("\nEmprestando livro:")
    emprestar_livro(session, "Dom Casmurro")

    print("\nDevolvendo livro:")
    devolver_livro(session, "Dom Casmurro")