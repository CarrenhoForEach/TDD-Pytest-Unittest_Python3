from src.leilao.dominio import Usuario, Leilao
from src.leilao.excecoes import LanceInvalido

import pytest

@pytest.fixture
def vini():
    return Usuario("Vini", 100.0)

@pytest.fixture
def leilao():
    return Leilao("TV")

def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_lance(vini, leilao):

    vini.propoe_lance(leilao, 50.0)
    
    assert vini.carteira == 50.0

def test_deve_permitir_valor_menor_carteira(vini, leilao):

    vini.propoe_lance(leilao, 1.0)

    assert vini.carteira == 99.0

def test_deve_permitir_lance_igual_carteira(vini, leilao):

    vini.propoe_lance(leilao, 100.0)

    assert vini.carteira == 0.0

def test_nao_deve_permitir_valor_maior_carteira(vini, leilao):
    
    with pytest.raises(LanceInvalido):

        vini.propoe_lance(leilao, 200.0)

        assert vini.carteira == 100.0