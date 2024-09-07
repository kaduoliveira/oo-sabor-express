class Livro:
    def __init__(self, titulo='', autor='', paginas=0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f'{self.titulo} por {self.autor} - {self.paginas} páginas'

    @property
    def titulo_autor(self):
        return f'{self.titulo} por {self.autor}'

    def aumentar_paginas(self, quantidade):
        self.paginas += quantidade

        '''Agora é sua vez! Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. Adicione um método especial __str__ para imprimir uma representação em string da pessoa. Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano. Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.'''

class Pessoa:
    pessoas = []

    def __init__(self, nome, idade, profissao):
        self.nome = nome.title()
        self.idade = idade
        self.profissao = profissao.upper()
        Pessoa.pessoas.append(self)
    
    def __str__(self):
        return f'{self.nome} - {self.idade} anos - {self.profissao}'
    
    @classmethod
    def listar_pessoas(cls):
        for pessoa in cls.pessoas:
            print(f'{pessoa.nome} - {pessoa.idade} anos - {pessoa.profissao}')

pessoa1 = Pessoa('laura', 9, 'filha 1')
pessoa2 = Pessoa('helena', 2, 'filha 2')

print(pessoa1)
print(pessoa2)

Pessoa.listar_pessoas()