import pygame

#inicializar
pygame.init()

tamanho_tela = (800, 800)
tela = pygame.display.set_mode(tamanho_tela)

pygame.display.set_caption('Brick Breaker')

#config bola
tamanho_bola = 15
bola = pygame.Rect(100, 500, tamanho_bola, tamanho_bola)

#config jogador
tamanho_jogador = 100
jogador = pygame.Rect(10, 750, tamanho_jogador, 15)

tamanho_blocos = 50
quant_blocos_linhas = 8
quant_linhas_blocos = 5
total_blocos = quant_blocos_linhas * quant_linhas_blocos

def criar_blocos(quant_blocos_linhas, quant_linhas_blocos):
    blocos = []
    #criar blocos
    return blocos

cores = {
    "branco": (255, 255, 255),
    "preto": (0, 0, 0),
    "amarelo": (255, 255, 0),
    "azul": (0, 0, 255),
    "verde": (0, 255, 0)
}

fim_jogo = False
pontuacao = 0
movimento_bola = [1, 1]

#criar as funcoes do jogo

#desenhas coisas na tela

tela.fill(cores["preto"])

#criar um loop infinito

while not fim_jogo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim_jogo = True

    pygame.time.wait(1)
    pygame.display.flip()

pygame.quit()