from hora_da_pratica_aula04 import Livro

#Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.

#No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.

livro_biblioteca = Livro('Cinderela', 'Disney', 1700)
print(f'O livro "{livro_biblioteca.titulo}" do autor {livro_biblioteca.autor} está disponivel? {livro_biblioteca.disponivel}')
#Livro.emprestar(livro_biblioteca)
print(f'O livro "{livro_biblioteca.titulo}" do autor {livro_biblioteca.autor} está disponivel? {livro_biblioteca.disponivel}')

#No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.
ano_especifico = 1994
livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)
print(f"Livros disponíveis em {ano_especifico}: {livros_disponiveis_ano}")