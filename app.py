import os
from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.item_cardapio import ItemCardapio
from modelos.cardapio.sobremesa import Sobremesa

restaurante1 = Restaurante('Praca', 'Gourmet')
restaurante2 = Restaurante('Mexican Food', 'Mexicana')
restaurante3 = Restaurante('Japa', 'Japones')

restaurante1.receber_avaliacao('Laura', 10)
restaurante1.receber_avaliacao('Helena', 5)
restaurante1.receber_avaliacao('Pituca', 6)

Restaurante.alternar_status(restaurante2)

prato1 = Prato('Macarronada', 14.9, 'Espaguete bolonhesa')
bebida1 = Bebida('Suco de manga', 5.0, '300ml')
bebida2 = Bebida('Coca-cola', 4.00, 'lata 350ml')
prato2 = Prato('Lasanha', 19.90, 'Massa em camadas a bolonhesa')
prato2.aplicar_desconto()
bebida2.aplicar_desconto()
sobremesa1 = Sobremesa('Pudim', 8.00, 'gelada', '100g', 'A base de leite com calda de caramelo')
sobremesa1.aplicar_desconto()

restaurante1.adicionar_no_cardapio(bebida1)
restaurante1.adicionar_no_cardapio(prato1)
restaurante1.adicionar_no_cardapio(bebida2)
restaurante1.adicionar_no_cardapio(prato2)
restaurante1.adicionar_no_cardapio(sobremesa1)

def main():
    os.system('cls')
    restaurante1.exibir_cardapio
    print(sobremesa1)
    

if __name__ == '__main__':
    main()