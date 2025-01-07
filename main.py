import pygame
from cobra import Cobra
from comida import Comida
import random

def mostrar_tela_fim_de_jogo(tela, pontos):
    # Função que exibe a tela de fim de jogo com a pontuação e os botões
    tela.fill((0, 0, 0))

    # Exibir a pontuação
    font = pygame.font.SysFont(None, 48)
    texto_pontos = font.render(f"Pontuação: {pontos}", True, (255, 255, 255))
    tela.blit(texto_pontos, (250, 150))

    # Exibir o botão "Novo Jogo"
    font_botao = pygame.font.SysFont(None, 36)
    texto_novo_jogo = font_botao.render("Novo Jogo", True, (0, 255, 0))
    retangulo_novo_jogo = pygame.Rect(225, 250, 150, 50)
    pygame.draw.rect(tela, (255, 255, 255), retangulo_novo_jogo)
    tela.blit(texto_novo_jogo, (235, 260))

    # Exibir o botão "Sair"
    texto_sair = font_botao.render("Sair", True, (255, 0, 0))
    retangulo_sair = pygame.Rect(225, 320, 150, 50)
    pygame.draw.rect(tela, (255, 255, 255), retangulo_sair)
    tela.blit(texto_sair, (270, 330))

    pygame.display.update()

    # Esperar o clique para novo jogo ou sair
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if retangulo_novo_jogo.collidepoint(evento.pos):
                    return True  # Novo jogo
                elif retangulo_sair.collidepoint(evento.pos):
                    rodando = False  # Fechar o jogo

    return False  # Caso o jogador saia

def main():
    pygame.init()

    # Configurações do jogo
    largura, altura = 600, 400
    tamanho = 20
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Jogo da Cobrinha - POO")
    relogio = pygame.time.Clock()

    # Instâncias das classes
    cobra = Cobra(largura // 2, altura // 2, tamanho)
    comida = Comida(random.randint(0, (largura - tamanho) // tamanho) * tamanho,
                    random.randint(0, (altura - tamanho) // tamanho) * tamanho,
                    tamanho)

    # Loop do jogo
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    cobra.mudar_direcao("CIMA")
                elif evento.key == pygame.K_DOWN:
                    cobra.mudar_direcao("BAIXO")
                elif evento.key == pygame.K_LEFT:
                    cobra.mudar_direcao("ESQUERDA")
                elif evento.key == pygame.K_RIGHT:
                    cobra.mudar_direcao("DIREITA")

        cobra.mover()

        if cobra._corpo[0][0] == comida._x and cobra._corpo[0][1] == comida._y:
            cobra.comer()
            comida.reposicionar(largura, altura)

        if cobra.colidiu(largura, altura):
            if mostrar_tela_fim_de_jogo(tela, cobra.pontos):
                # Novo jogo
                cobra = Cobra(largura // 2, altura // 2, tamanho)
                comida = Comida(random.randint(0, (largura - tamanho) // tamanho) * tamanho,
                                random.randint(0, (altura - tamanho) // tamanho) * tamanho,
                                tamanho)
            else:
                rodando = False  # Fechar o jogo após sair

        tela.fill((0, 0, 0))
        cobra.desenhar(tela)
        comida.desenhar(tela)
        pygame.display.update()
        relogio.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()
