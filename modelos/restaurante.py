'''class Musica():
    nome = ''
    artista = ''
    duracao = int

musica1 = Musica()
musica1.nome = 'Bohemian Rhapsody'
musica1.artista = 'Queen'
musica1.duracao = 355

musica2 = Musica()
musica2.nome = 'Imagine'
musica2.artista = 'Beatles'
musica2.duracao = 183

musica3 = Musica()
musica3.nome = 'Shape of you'
musica3.artista = 'Ed Sheeran'
musica3.duracao = 234

print(vars(musica3))'''

class Restaurante:
    restaurantes = [] #a classe Restaurantes vai ter uma lista dentro de si para uso livre

    def __init__(self, nome, categoria): #expressão construtora
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False #usando _ eu torno o atributo privado, nao acessivel de forma direta
        Restaurante.restaurantes.append(self) #o construtor tá incluindo um novo valor no dicionario restaurantes sempre q um novo objeto é instanciado

    def __str__(self):
        return f'{self._nome} | {self._categoria}' #sempre q solicitarmos o objeto e for necessário a sua exibição em string ele usara esse metodo
    
    @classmethod
    def listar_restaurantes(cls): #metodo criado especificamente para esse uso, vai listar os rstaurantes presentes no dicionario contido na classe
        print(f'{'Nome do Restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {restaurante.ativo}')
    
    @property
    def ativo(self):
        return 'Ativado' if self._ativo else 'Desativado' #retonar ok se ativo q chama ele mesmo for True e caixa vazia se for false

    def alternar_status(self):
        self._ativo = not self._ativo #o atributo _ativo recebe ele mesmo invertido ja que usamos a função not

    
restaurante_praca = Restaurante('Praça', "Gourmet") #instanciando oobjeto
restaurante_praca._nome = 'Pizza 2.0'
restaurante_praca.alternar_status()
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

Restaurante.listar_restaurantes()



'''if restaurante_praca.ativo:
    print('O restaurante está ☑.')
else:
    print('O restaurante está ☐.')
    print('O restaurante está ☑')'''