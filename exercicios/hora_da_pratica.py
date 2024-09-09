'''Desafios

Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.

Crie uma instância da classe e imprima o valor da propriedade titular.

Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.

Crie um método de classe para a conta ClienteBanco.'''

class ContaBancaria:
    contas = []

#Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.
    def __init__(self, titular, saldo):
        self._titular = titular.title()
        self._saldo = saldo
        self._ativo = False
        ContaBancaria.contas.append(self)
    
    #Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.
    def __str__(self):
        return f'Olá {self._titular.upper()}, seu saldo é R$ {self._saldo}, sua conta está {self._ativo}'
    
    #Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True
    
    @property
    def ativo(self):
        return 'Ativa' if self._ativo else 'Desativada'

    '''def listar_clientes(cls):
        for conta in cls.contas:
            print(f'Olá {conta._titular.upper()}, seu saldo é R$ {conta._saldo} zzz')'''

cliente1 = ContaBancaria('josé', 455.98)
cliente1.ativar_conta(cliente1)
cliente2 = ContaBancaria('helena', 22468.888)

print(cliente1)
print(cliente2)

