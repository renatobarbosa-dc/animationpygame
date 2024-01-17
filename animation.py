import pygame
import sys
import os

pygame.init()

# Configurações da tela
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Personagem Andando e Pulando")

# Cores
black = (0, 0, 0)

# Personagem
personagem_largura = 50
personagem_altura = 50
personagem_x = largura_tela // 2 - personagem_largura // 2
personagem_y = altura_tela - personagem_altura - 10
personagem_velocidade = 5
personagem_velocidade_y = 0
pulo = False

# Carregando imagens da animação
caminho_imagens = os.path.join(os.path.dirname(__file__), 'sprites')
imagens_andando_direita = [pygame.image.load(os.path.join(caminho_imagens, 'sprites/marioframe1.png')),
                           pygame.image.load(os.path.join(caminho_imagens, 'sprites/marioframe2.png')),
                           pygame.image.load(os.path.join(caminho_imagens, 'sprites/marioframe3.png')),
                           pygame.image.load(os.path.join(caminho_imagens, 'sprites/marioframe4.png'))]

imagens_andando_esquerda = [pygame.transform.flip(img, True, False) for img in imagens_andando_direita]

imagens_pulo = [pygame.image.load(os.path.join(caminho_imagens, 'marioframe5.png'))]


imagens_pulo_direita = [pygame.transform.flip(img, True, False) for img in imagens_pulo]


# Imagem inicial
indice_animacao = 0
personagem_direcao = 'direita'
personagem_img = imagens_andando_direita[indice_animacao]

# Gravidade
gravidade = 1

# Velocidade ao correr
velocidade_andando = 5
velocidade_correndo = 10
correndo = False

# Loop principal
clock = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Captura das teclas pressionadas
    teclas = pygame.key.get_pressed()

    # Verifica se a tecla Shift está pressionada para correr
    correndo = teclas[pygame.K_LSHIFT] or teclas[pygame.K_RSHIFT]

    # Movimento para a esquerda
    if teclas[pygame.K_LEFT] and personagem_x > 0:
        personagem_x -= velocidade_correndo if correndo else velocidade_andando
        if not pulo:
            if correndo:
                indice_animacao = (indice_animacao + 1) % len(imagens_correndo_esquerda)
                personagem_img = imagens_correndo_esquerda[indice_animacao]
            else:
                indice_animacao = (indice_animacao + 1) % len(imagens_andando_esquerda)
                personagem_img = imagens_andando_esquerda[indice_animacao]
        personagem_direcao = 'esquerda'

    # Movimento para a direita
    if teclas[pygame.K_RIGHT] and personagem_x < largura_tela - personagem_largura:
        personagem_x += velocidade_correndo if correndo else velocidade_andando
        if not pulo:
            if correndo:
                indice_animacao = (indice_animacao + 1) % len(imagens_correndo_direita)
                personagem_img = imagens_correndo_direita[indice_animacao]
            else:
                indice_animacao = (indice_animacao + 1) % len(imagens_andando_direita)
                personagem_img = imagens_andando_direita[indice_animacao]
        personagem_direcao = 'direita'

    # Pulo
    if not pulo:
        if teclas[pygame.K_SPACE]:
            personagem_velocidade_y = -15
            pulo = True
            indice_animacao = 0

    else:
        if personagem_y < altura_tela - personagem_altura - 10:
            personagem_velocidade_y += gravidade
        else:
            personagem_velocidade_y = 0
            pulo = False
            personagem_y = altura_tela - personagem_altura - 10

        # Adiciona animação de virar durante o pulo
        if personagem_direcao == 'esquerda':
            personagem_img = imagens_pulo[indice_animacao]
        else:
            personagem_img = pygame.transform.flip(imagens_pulo[indice_animacao], True, False)

    # Restante do código permanece inalterado
    # Atualização da posição vertical
    personagem_y += personagem_velocidade_y

    # Se nenhuma tecla de movimento estiver pressionada, volte ao primeiro sprite
    if not teclas[pygame.K_LEFT] and not teclas[pygame.K_RIGHT]:
        indice_animacao = 0
        if correndo:
            personagem_img = imagens_correndo_direita[0] if personagem_direcao == 'direita' else imagens_correndo_esquerda[0]
        else:
            personagem_img = imagens_andando_direita[0] if personagem_direcao == 'direita' else imagens_andando_esquerda[0]

    # Atualização da tela
    tela.fill(black)

    # Atualização da tela (continuação)
    tela.blit(personagem_img, (personagem_x, personagem_y))
    pygame.display.flip()

    # Controle de taxa de atualização (aumentado para acelerar a animação)
    clock.tick(30)  # Experimente valores mais baix
