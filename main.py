import pygame

#inicializar
pygame.init()

nome = 'Victor'
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
    altura_tela = tamanho_tela[1]
    largura_tela = tamanho_tela[0]
    distancia_blocos = 5
    largura_bloco = largura_tela / quant_blocos_linhas - distancia_blocos
    altura_bloco = 15
    distancia_linhas = altura_bloco + 10

    blocos = []
    #criar blocos
    for j in range(quant_linhas_blocos):
        for i in range(quant_blocos_linhas):
            #criar o bloco
            bloco = pygame.Rect(i * (largura_bloco + distancia_blocos), j * distancia_linhas, largura_bloco, altura_bloco)
            #adicionar o bloco a lista
            blocos.append(bloco)       
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
movimento_bola = [1, -1]

#criar as funcoes do jogo
def movimentar_jogador(evento):
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_RIGHT:
            if (jogador.x + tamanho_jogador) < (tamanho_tela[0] - 1):
                jogador.x = jogador.x + 1
        if evento.key == pygame.K_LEFT:
            if jogador.x > 1:
                jogador.x = jogador.x - 1


def movimentar_bola(bola):
    movimento = movimento_bola
    bola.x = bola.x + movimento[0]
    bola.y = bola.y + movimento [1]

    if bola.x <= 0:
        movimento[0] = - movimento[0]
    if bola.y <= 0:
        movimento[1] = - movimento[1] 
    if (bola.x + tamanho_bola) >= tamanho_tela[0]:  
        movimento[0] = - movimento[0]
    if (bola.y + tamanho_bola) >= tamanho_tela[1]:
        movimento = None

    if jogador.collidepoint((bola.x + 13), (bola.y + 13)):
        movimento[1] = - movimento[1]
    for bloco in blocos:
        if bloco.collidepoint(bola.x, bola.y):
            movimento[1] = - movimento[1]
            blocos.remove(bloco)
    
    return movimento

def atualizar_pontuacao(pontuacao):
    fonte = pygame.font.Font(None, 30)
    texto = fonte.render(f"Pontuação: {pontuacao}", 1, cores["amarelo"])
    tela.blit(texto, (640, 775))
    if pontuacao >= total_blocos:
        return True
    else: False

def assinatura(nome):
    fonte = pygame.font.Font(None, 20)
    texto = fonte.render(f"by {nome}", 1, cores["branco"])
    tela.blit(texto, (10, 775))

#desenhas coisas na tela
def desenhar_inicio_jogo():
    tela.fill(cores["preto"])
    pygame.draw.rect(tela, cores["azul"], jogador)
    pygame.draw.rect(tela, cores["branco"], bola)

def desenhar_blocos(blocos):
    for bloco in blocos:
        pygame.draw.rect(tela, cores["verde"], bloco)
    
blocos = criar_blocos(quant_blocos_linhas, quant_linhas_blocos)
#criar um loop infinito

while not fim_jogo:
    desenhar_inicio_jogo()
    desenhar_blocos(blocos)
    assinatura(nome)
    fim_jogo = atualizar_pontuacao(total_blocos - len(blocos))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim_jogo = True

    movimentar_jogador(evento)
    movimento_bola = movimentar_bola(bola)
    if not movimento_bola:
        fim_jogo = True

    pygame.time.wait(1)
    pygame.display.flip()

pygame.quit()