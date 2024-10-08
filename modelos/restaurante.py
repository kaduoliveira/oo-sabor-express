from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = [] #a classe Restaurantes vai ter uma lista dentro de si para uso livre

    def __init__(self, nome, categoria): #expressão construtora
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False #usando _ eu torno o atributo privado, nao acessivel de forma direta
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self) #o construtor tá incluindo um novo valor no dicionario restaurantes sempre q um novo objeto é instanciado

    def __str__(self):
        return f'{self._nome} | {self._categoria} | {self._avaliacao}' #sempre q solicitarmos o objeto e for necessário a sua exibição em string ele usara esse metodo
    
    @classmethod
    def listar_restaurantes(cls): #metodo criado especificamente para esse uso, vai listar os rstaurantes presentes no dicionario contido na classe
        print(f'{'Nome do Restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Avaliação'.ljust(20)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} | {restaurante.ativo}')
    
    @property
    def ativo(self):
        return '☑' if self._ativo else '☐' #retonar ok se ativo q chama ele mesmo for True e caixa vazia se for false

    def alternar_status(self):
        self._ativo = not self._ativo #o atributo _ativo recebe ele mesmo invertido ja que usamos a função not

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
    
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
  
    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'\nCardápio do restaurante {self._nome}')
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'tipo'):
                mensagem_sobremesa = f'{i}. {item._nome} - R$ {item._preco} - {item.tipo} - {item.descricao}'
                print(mensagem_sobremesa)
            elif hasattr(item, 'descricao'):
                mensagem_prato = f'{i}. {item._nome} - R$ {item._preco} - {item.descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. {item._nome} - R$ {item._preco} - {item.tamanho}'
                print(mensagem_bebida)
        print()