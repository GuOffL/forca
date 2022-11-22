import jogo as d
import estagios as e

j = d.Jogo()

# Iniciar Jogo
j.start()
# Área de teste:
print(j.getPalavra())
# ===============================================
while True: 
# Usuario escolhe a letra
    letra_usuario = j.pega_letra('Escolha uma letra: \n')
# Verificar a letra do usuario
    j.confere(letra_usuario)



# Game Over
    if j.getVidas() == 0:
        print(e.morto)
        break