from hora_da_pratica_aula04 import Livro

livro_main1 = Livro("Python para Iniciantes", "Carlos Coder", 2021)
livro_main2 = Livro("Web Development Essentials", "Laura Developer", 2023)

#usando metodo __str__
print('\nUsando metodo __str__')
print(livro_main1)
print(livro_main2)

print('\nUsando metodo Listar_livros')
Livro.listar_livros()
