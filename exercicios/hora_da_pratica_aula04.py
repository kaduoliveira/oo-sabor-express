#Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.
class Livro:
    livros = []
    
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel =True
    
    #Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.
    def __str__(self):
        return f'Livro: {self.titulo.ljust(20)} | Autor: {self.autor.ljust(15)} | Ano: {str(self.ano_publicacao).ljust(5)} | Disp.: {self.disponivel}'
    
    #Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.
    
    def emprestar(self):
        self.disponivel = not self.disponivel


    #Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.
    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel == True]
        return livros_disponiveis

livro1 = Livro('O senhor dos aneis', 'J R R Tolkien', 1948)
livro2 = Livro('Game of Thrones', 'J R R Martin', 1994)
livro3 = Livro('O alquimista', 'Paulo Coelho', 1992)

Livro.livros= [livro1, livro2, livro3]

print(livro1)
Livro.emprestar(livro2)
print(livro2)








#Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str.

