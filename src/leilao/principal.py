from src.leilao.dominio import Usuario, Leilao, Lance, Avaliador

thi = Usuario("Thiago Carrenho Ferreira")
dani = Usuario("Danilo Carrenho Ferreira")

thi_lance = Lance(thi, 6500)
dani_lance = Lance(dani, 6250)

leilao = Leilao("Laptop")

leilao.lances.append(dani_lance)
leilao.lances.append(thi_lance)


for lance in leilao.lances:
    print(f"O cliente {lance.usuario.nome} deu um lance de {lance.valor} no laptop em questão")

avaliador = Avaliador()

avaliador.avalia(leilao)

print(f"o menor lance foi de {avaliador.menor_lance} e o maior lance foi de {avaliador.maior_lance}")