'''
    COMPILADO DE FUNCOES UTEIS DIVERSAS

    - checkPointOnRec() -> utilizada para checar a presenca de um ponto em um retangulo qualquer
    - draw_text_with_border() -> desenha textos com fontes customizaveis com bordas coloridas nas letras

'''
import pyxel
import os

#FUNCAO USADA PARA DESENHAR CONTEUDO DE UM TILEMAP N (com dimensoes x, y)
def draw_tilemapItens(pyxel, tilemap, sprite_bank, ALTURA, LARGURA, TAMANHO, ESCALA):
        #percorrendo tilemap nas dimensoes repassadas
        for y in range(ALTURA):
            for x in range(LARGURA):
                item = tilemap.pget(x, y) #coletando info do tilemap
                #desenhando item coletado
                pyxel.blt( 
                14 + x * TAMANHO * ESCALA, #posicao X onde sera desenhado o item (+14 como ajuste manual)
                10 + y * TAMANHO * ESCALA, #posicao Y onde sera desenhado o item (+10 como ajuste manual)
                sprite_bank, #especificando qual banco de sprites sera usado de referencia para desenhar
                item[0] * TAMANHO, #posicao X do sprite no tilemap
                item[1] * TAMANHO, #posicao Y do sprite no tilemap
                TAMANHO, #dimensao X do item
                TAMANHO, #dimensao Y do item
                scale=ESCALA
                )

#FUNCAO USADA PARA DESENHAR UM PLANO CARTESIANO DE DIMENSOES (X, Y) 
def drawCartesianPlan(inicioX, inicioY, largura, altura, tam):
    #desenhando eixos do plano cartesiano x,y
    pyxel.line(inicioX, inicioY+(altura/2), inicioX+largura, inicioY+(altura/2), pyxel.COLOR_GREEN) #eixo X
    pyxel.line(inicioX+(largura/2), inicioY, inicioX+(largura/2), inicioY+altura, pyxel.COLOR_RED) #eixo Y
    #desenhando medidores (de tamanho=tam) ao longo dos eixos para nocoes de escala
    quantidadeX = int(largura/tam)
    quantidadeY = int(altura/tam)
    for i in range(quantidadeX+1):
        pyxel.line(inicioX+(i*tam), inicioY+(altura/2)-(tam/2), inicioX+(i*tam), inicioY+(altura/2)+(tam/2), pyxel.COLOR_YELLOW)
    for i in range(quantidadeY+1):
        pyxel.line(inicioX+(largura/2)-(tam/2), inicioY+(i*tam), inicioX+(largura/2)+(tam/2), inicioY+(i*tam), pyxel.COLOR_YELLOW)


#FUNCAO USADA PARA CHECAR COLISAO DE UM PONTO (x, y) COM UM RETANGULO (x, y, largura, altura)
def checkPointOnRec(posX, posY, recX, recY, largura, altura):
    #checando se ponto de coordenada (X, Y) se encontra dentro de retangulo com as dimensoes passadas
    if ( posX >= recX and posX <= recX+largura and posY >= recY and posY <= recY+altura):
        return True
    else:
        return False

'''
Funcao usada para: 
    -> desenhar bordas nas letras de uma palavra "S" de letras
    -> dar coloracao "col" para as letras e coloracao "bcol" para a borda
    -> gerar palavra final de acordo com a fonte "font"
'''
def draw_text_with_border(x, y, s, col, bcol, font):
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx != 0 or dy != 0:
                pyxel.text(
                    x + dx,
                    y + dy,
                    s,
                    bcol, #valor para colorir a borda das letras
                    font, #arquivo da fonte para as letras
                )
    pyxel.text(x, y, s, col, font)
