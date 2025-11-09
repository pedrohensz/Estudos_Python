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
    def ativar_conta(csl,conta): #aqui no classmetho, a conta é uma variável já que não chamamos o self por ser um método de classe
        conta._ativo = True

C1 = ContaBancaria("Pedro",1200.00)
C1.ativar_conta(C1)
print(C1)
