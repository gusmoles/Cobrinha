# Cobrinha
Jogo da cobrinha para a aula de orientação a objetos
Este projeto implementa um jogo da cobrinha em Python utilizando a biblioteca Pygame, com o uso de Programação Orientada a Objetos (POO). O jogo permite ao jogador controlar a cobra e coletar maçãs para aumentar sua pontuação e tamanho, enquanto evita colidir com as bordas da tela e consegue mesma.

Estrutura do Código
O código é organizado em diferentes arquivos e classes, cada um responsável por uma parte específica do jogo.

Arquivos e Suas Funções
entidade.py

ClasseEntidade :

Serve como classe base para qualquer objeto do jogo. Contém os atributos de posição ( x, y) e tamanho ( tamanho) e define o método desenhar(), que deve ser implementado pelas subclasses para desenhar o objeto na tela.
Propósito :

Facilitar a reutilização de código para diferentes entidades do jogo, como a cobra e a comida, garantindo que todas as entidades tenham atributos básicos de posição e tamanho.
cobra.py

ClasseCobra :

Herda da classe Entidadee representa a cobra no jogo. A classe gerencia o movimento da cobra, o crescimento dela quando chega, a mudança de direção e a seleção de colisões.
Possui atributos como:
_corpo: Lista que armazena as posições dos segmentos da cobra.
_direcao: A direção atual da cobra (cima, baixo, esquerda, direita).
_crescer: Indica se a cobra deve crescer após comer a comida.
pontos: Contabiliza os pontos do jogador.
Principais funções :

mover(): Mova a cobra de acordo com a direção escolhida.
mudar_direcao(direcao): Altere a direção da cobra, respeitando a restrição de não permitir que ela mude para a direção oposta.
comer(): Aumenta a pontuação e marca a cobra para crescer.
desenhar(tela): Desenha a cobra na tela, incluindo os segmentos do corpo e dos olhos.
colidiu(largura, altura): Verifique se a cobra colidiu com as bordas ou com ela mesma.
Propósito :

Gerenciar a lógica da cobra, incluindo movimento, crescimento e colisões.
comida.py

ClasseComida :

Herda de Entidadee representa a comida (a maçã) que a cobra deve comer. A aula gerencia o desenho da maçã na tela e seu reposicionamento aleatório após ser comida pela cobra.
A imagem da maçã é enviada diretamente da web (utilizando o link da imagem) e redimensionada para o tamanho especificado.
Principais funções :

desenhar(tela): Desenha a comida (maçã) na tela.
reposicionar(largura, altura): Reposiciona a comida aleatoriamente dentro da tela.
Propósito :

Forneça a comida que a cobra deve comer, alterando sua posição aleatoriamente a cada vez que a cobra consumir.
main.py

Função principal ( main()) :

Contém o loop principal do jogo. Inicializa o Pygame, define a tela e o tamanho da janela, e cria as instâncias da cobra e da comida.
Dentro do loop, o jogo responde às teclas pressionadas (setas para movimento da cobra) e gerencia o movimento, crescimento e colisões da cobra.
Quando uma cobra chega à comida, a pontuação aumenta e a comida é reposicionada.
Se a cobra colide com as bordas ou com ela mesma, uma tela de fim de jogo é exibida, permitindo ao jogador iniciar um novo jogo ou sair.
Funções adicionais :

mostrar_tela_fim_de_jogo(tela, pontos): Exibe a tela de fim de jogo com a pontuação final e opções de reiniciar o jogo ou sair.
Propósito :

Orquestrar o jogo, controlando a lógica do loop e o gerenciamento de eventos (movimento da cobra, alimentação e colisões).
Como Funciona
Movimento da Cobra :

A cobra se move na direção definida pelas teclas de seta. O método mover()é responsável por atualizar a posição da cobra com base na direção atual.
Crescimento da Cobra :

Cada vez que uma cobra “vem” a comida, ela cresce (um novo segmento é adicionado ao corpo) e a classificação aumenta. Isso é gerido pelo método comer().
Verificação de Colisões :

A cobra verifica se bateu nas bordas ou em seu próprio corpo usando o método colidiu(). Caso haja dúvidas, o jogo termina.
Reinício do Jogo :

Quando o jogo termina, o jogador pode reiniciar a partida ou sair. Isso é feito através de uma tela de fim de jogo exibida pela função mostrar_tela_fim_de_jogo().
Observações Finais
Desempenho : A velocidade do jogo é controlada pela função relogio.tick(10), que define a quantidade de quadros por segundo (FPS). O valor 10 pode ser ajustado para tornar o jogo mais rápido ou mais lento.
Imagem da Comida : A maçã é fornecida a partir de um link de imagem da web, o que pode afetar o desempenho dependendo da conexão com a internet. A imagem é redimensionada para ser ajustada ao tamanho da comida.


---


## Instruções para Execução

1. Certifique-se de que o Python 3 está instalado em sua máquina.
2. Instale o Pygame utilizando o comando:

   ```bash
   pip install pygame
3. Clone este repositório:
   
   ```bash
     git clone https://github.com/gusmoles/Cobrinha.git

4. Navegue até a pasta do projeto e execute o jogo:
   ```bash
   python main.py




