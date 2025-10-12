
import pygame

# Inicialização
pygame.init()
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
tela1 = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Quadrado Móvel")

# Cores
VERMELHO = (255, 0, 0)
PRETO = (0, 0, 0)
VERDE = (0, 128, 0)

# Variáveis do quadrado

tamanho_vermelho = 50
x_vermelho = largura // 2 - tamanho_vermelho // 2
y_vermelho = altura // 2 - tamanho_vermelho // 2
velocidade_vermelho = 5

tamanho_verde = 50
x_verde = largura // 4 - tamanho_verde // 2
y_verde = altura // 4 - tamanho_verde // 2
velocidade_verde = 5

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    
    # Controles do teclado (COMPLETE AQUI)
    
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w]:
        y_vermelho -= velocidade_vermelho
    if teclas[pygame.K_s]:
        y_vermelho += velocidade_vermelho
    if teclas[pygame.K_a]:
        x_vermelho -= velocidade_vermelho
    if teclas[pygame.K_d]:
        x_vermelho += velocidade_vermelho

   
    if teclas[pygame.K_UP]:
        y_verde -= velocidade_verde
    if teclas[pygame.K_DOWN]:
        y_verde += velocidade_verde
    if teclas[pygame.K_LEFT]:
        x_verde -= velocidade_verde
    if teclas[pygame.K_RIGHT]:
        x_verde += velocidade_verde
    
    # Limitar à tela (DESAFIO EXTRA)
    x_vermelho = max(400, min(x_vermelho, largura - tamanho_vermelho))
    y_vermelho = max(300, min(y_vermelho, altura - tamanho_vermelho))

    # Limitar à tela para o quadrado verde
    x_verde = max(0, min(x_verde, largura - tamanho_verde))
    y_verde = max(0, min(y_verde, altura - tamanho_verde))
    
    # Desenho
    tela.fill(PRETO)
    pygame.draw.rect(tela, VERMELHO, (x_vermelho, y_vermelho, tamanho_vermelho, tamanho_vermelho))

    pygame.draw.rect(tela1, VERDE, (x_verde, y_verde, tamanho_verde, tamanho_verde))

    pygame.display.update()


pygame.quit()