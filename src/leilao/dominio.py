#import sys
from src.leilao.excecoes import LanceInvalido

class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    def propoe_lance(self, leilao, valor):
        #if valor > self.__carteira:
        if not self._valor_eh_maior(valor):
            raise LanceInvalido("O valor não pode ser maior que a carteira!!!")

        lance = Lance(self, valor)
        leilao.propoe(lance)

        self.__carteira -= valor

    def _valor_eh_maior(self, valor):
        return valor <= self.__carteira

    @property
    def carteira(self):
        return self.__carteira

    @property
    def nome(self):
        return self.__nome


class Lance:

    def __init__(self, usuario, valor):
        
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        #self.maior_lance = sys.float_info.min
        #self.menor_lance = sys.float_info.max
        self.menor_lance = 0.0
        self.maior_lance = 0.0

        self.descricao = descricao
        self.__lances = []

    def propoe(self, lance:Lance):
        #if not self.__lances or self.__lances[-1].usuario != lance.usuario and lance.valor > self.__lances[-1].valor:
        #if not self._tem_lance() or self._usuarios_diferentes(lance) and self._valor_maior_que_ultimo_lance(lance):
            #if not self.__lances:
        if self._lance_eh_valido(lance):
            if not self._tem_lance():
                self.menor_lance = lance.valor
            self.maior_lance = lance.valor
           
            self.__lances.append(lance)

        #else:
            #raise LanceInvalido("Erro ao propor lance!!!")

    def _lance_eh_valido(self, lance):
        return not self._tem_lance() or (self._usuarios_diferentes(lance) and 
                                                    self._valor_maior_que_ultimo_lance(lance))

    def _valor_maior_que_ultimo_lance(self, lance):
        if lance.valor > self.__lances[-1].valor:
            return True
        raise LanceInvalido("O lance tem que ser maior que o último!!!")
    
    def _usuarios_diferentes(self, lance):
        if self.__lances[-1].usuario != lance.usuario:
            return True
        raise LanceInvalido("O mesmo usuário não pode dar lance seguidos!!!")

    def _tem_lance(self):
        return self.__lances


        '''
            if lance.valor > self.maior_lance:
                    self.maior_lance = lance.valor
            if lance.valor < self.menor_lance:
                    self.menor_lance = lance.valor
        '''

    @property
    def lances(self):
        return self.__lances[:]
'''
class Avaliador:
    def __init__(self):
        self.maior_lance = sys.float_info.min
        self.menor_lance = sys.float_info.max

    def avalia(self, leilao:Leilao):

        for lance in leilao.lances:
            if lance.valor > self.maior_lance:
                self.maior_lance = lance.valor
            if lance.valor < self.menor_lance:
                self.menor_lance = lance.valor
'''
