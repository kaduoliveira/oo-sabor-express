import os
from modelos.restaurante import Restaurante

restaurante1 = Restaurante('Praca', 'Gourmet')
restaurante2 = Restaurante('Mexican Food', 'Mexicana')
restaurante3 = Restaurante('Japa', 'Japones')

restaurante1.receber_avaliacao('Laura', 10)
restaurante1.receber_avaliacao('Helena', 5)
restaurante1.receber_avaliacao('Pituca', 6)

Restaurante.alternar_status(restaurante2)

def main():
    os.system('cls')
    Restaurante.listar_restaurantes()
    

if __name__ == '__main__':
    main()