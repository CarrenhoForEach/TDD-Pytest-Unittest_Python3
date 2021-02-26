from unittest import TestCase
from src.leilao.dominio import Usuario, Leilao, Lance
from src.leilao.excecoes import LanceInvalido

class TestAvaliador(TestCase):

    def setUp(self):
        self.thi = Usuario("Thiago Carrenho Ferreira", 500.0)
        
        self.thi_lance = Lance(self.thi, 6500)

        self.leilao = Leilao("Laptop")

    def test_deve_avaliar_os_lances_quando_em_ordem_crescente(self):
        dani = Usuario("Danilo Carrenho Ferreira", 500.0)
        dani_lance = Lance(dani, 6250)

        self.leilao.propoe(dani_lance)
        self.leilao.propoe(self.thi_lance)
        
        '''
        avaliador = Avaliador()

        avaliador.avalia(self.leilao)
'''
        menor_valor_esperado = 6250
        maior_valor_esperado = 6500
        
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance) 
        
    def test_deve_avaliar_os_lances_quando_em_ordem_decrescente(self):
        with self.assertRaises(LanceInvalido):
            dani = Usuario("Danilo Carrenho Ferreira", 500.0)
            dani_lance = Lance(dani, 6250)
            
            self.leilao.propoe(self.thi_lance)
            self.leilao.propoe(dani_lance)
        '''
        avaliador = Avaliador()

        avaliador.avalia(self.leilao)
'''
        #menor_valor_esperado = 6250
        #maior_valor_esperado = 6500
        
        #self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        #self.assertEqual(maior_valor_esperado, self.leilao.maior_lance) 
    
    def test_deve_avaliar_um_unico_lance(self):
        self.leilao.propoe(self.thi_lance)
        '''
        avaliador = Avaliador()

         avaliador.avalia(self.leilao)
        '''
        self.assertEqual(6500, self.leilao.menor_lance)
        self.assertEqual(6500, self.leilao.maior_lance)    

    def test_deve_avaliar_tres_lances(self):
        su = Usuario("Sueli Carrenho", 500.0)
        dani = Usuario("Danilo Carrenho Ferreira", 500.0)
        
        su_lance = Lance(su, 8500)
        dani_lance = Lance(dani, 6250)

        leilao = Leilao("Nintendo Switch")
        
        leilao.propoe(dani_lance) 
        leilao.propoe(self.thi_lance)
        leilao.propoe(su_lance)
        '''
        avaliador = Avaliador()

        avaliador.avalia(leilao)
        '''
        menor_valor_esperado = 6250
        maior_valor_esperado = 8500
        
        self.assertEqual(menor_valor_esperado, leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, leilao.maior_lance) 

    def test_deve_permitir_lance_caso_seja_o_primeiro(self):
        self.leilao.propoe(self.thi_lance)

        quantidade_de_lances = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances)
    
    def test_ultimo_lance_usuario_diferente(self):
        matheus = Usuario("Matheus Soares", 500.0)
        lance_do_matheus = Lance(matheus, 200)
        self.leilao.propoe(lance_do_matheus)
        self.leilao.propoe(self.thi_lance)

        quantidade_de_lances = len(self.leilao.lances)

        self.assertEqual(2, quantidade_de_lances)
    
    def test_um_usuario_nao_pode_dar_lance_seguidos(self):
        thi_lance_9000 = Lance(self.thi, 9000)
        
        #try:
        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(thi_lance_9000)
            self.leilao.propoe(self.thi_lance)
            #self.fail(msg="Não lançou exceção")
        '''except ValueError:
            quantidade_lances = len(self.leilao.lances)
            self.assertEqual(1, quantidade_lances)
        '''