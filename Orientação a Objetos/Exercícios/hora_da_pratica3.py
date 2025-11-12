"""
1 -Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.
"""
class ContaBancaria:
    def __init__(self, titular, saldo, ativo):
        self.titular = titular
        self.saldo = saldo
        self.ativo = False

"""
Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.
"""
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False
    
    def __str__(self):
        return f"Titular: {self.titular} | Saldo: R${self.saldo}"
    

C1 = ContaBancaria("Pedro",1200.00)
C2 = ContaBancaria("Henrique",1000.00)

#print(C1)
#print(C2)

"""Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo."""

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False
    
    def __str__(self):
        return f"Titular: {self.titular} | Saldo: R${self.saldo}"
    
    @classmethod
    def ativar_conta(csl,conta): #aqui no classmethod, a conta é uma variável já que não chamamos o self por ser um método de classe
        conta._ativo = True

C1 = ContaBancaria("Pedro",1200.00)
C1.ativar_conta(C1)
# print(C1)

"""
Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.
"""
"""esse exercício eu pedi auxílio da IA por que eu não entendi muito bem a abordagem "pythonica.
No gabarito foi feito apenas o uso de atributos internos e o uso de property para acesso controlado dos atributos, aqui eu acabei utilizando getters e setters 
"""

class ContaBancaria:
    def __init__(self, _titular, _saldo):
        self._titular = _titular
        self._saldo = _saldo
        self._ativo = False
    
    def __str__(self):
        return f"Titular: {self._titular} | Saldo: R${self._saldo}"
    
    @property
    def titular(self):
        return f"Titular: {self._titular}"

    @titular.setter
    def titular(self, novo_titular):
        if not isinstance(novo_titular, str):
            raise TypeError ("O titular precisa ser uma string.")
        elif not novo_titular.strip():
            raise ValueError ("O titular está vazio.")   
        else:
            self._titular = str(novo_titular)
    
    
    @property
    def saldo(self):
        return f"O seu saldo é de: {self._saldo}"

    @saldo.setter
    def saldo(self, novo_saldo):
        if not isinstance(novo_saldo, float):
            raise TypeError ("O valor inserido precisa conter vírgulas.")
        elif novo_saldo < 0:
            raise ValueError ("O saldo inserido está negativo")   
        else:
            self._titular = int(novo_saldo)
    
        

    @classmethod
    def ativar_conta(csl,conta): #aqui no classmetho, a conta é uma variável já que não chamamos o self por ser um método de classe
        conta._ativo = True

C1 = ContaBancaria("Pedro",1200.00)

C1._titular = "Pedro"
C1._saldo = 1200.00
print(C1._titular)
print(C1._saldo)


"""
Crie uma instância da classe e imprima o valor da propriedade titular.
"""
C1 = ContaBancaria("Pedro",1200.00)
print(f"O titular da conta é {C1._titular}")

"""
Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.

"""

class ClienteBanco:
    def __init__(self,titular,saldo,credito,score):
        self.titular = titular
        self.saldo = saldo
        self.credito = credito
        self.score = score
        self.ativo = False
    
    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = (titular, saldo_inicial)
        return f"Conta de {titular} criada com saldo inicial de {saldo_inicial}"
    
    def __str__(self):
        return f"Titular: {self.titular} | Saldo: {self.saldo}"

C1 = ClienteBanco("Pedro", 1000.00, 100000.00,1000)
C2 = ClienteBanco("Lucas", 50000.00, 1000000.00,1000)
C3 = ClienteBanco("Cleber", 200.00, 5000.00,600)

C4 = ClienteBanco.criar_conta("Julia", 400)
