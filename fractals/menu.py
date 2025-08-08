'''
    PROGRAMA AUXILIAR RESPONSAVEL POR INICIALIZAR O MENU DE FRACTAL 1.0

    -> Conta com uma interface simples, onde  o usuario podera escolher
    qual fractal iniciar...ou entao sair da aplicacao
'''

from models import utilities
from fractals import State
import pyxel

#CODIGO PRINCIPAL
class Menu(State):

    def onEnter(self, game):
        #inicializando janela
        pyxel.mouse(True)
        #carregando icones do jogo
        pyxel.load("/home/hacdan/Documents/Linux/Programacao/Python/Projetos/Pyxel/FRACTALS_1.0/Assets/ICONES_FRACTAIS.pyxres")
        #carregando fonte das letras
        self.fonte16 = pyxel.Font("/home/hacdan/Documents/Linux/Programacao/Python/Projetos/Pyxel/FRACTALS_1.0/Assets/Fonts/b16_b.bdf")
        self.fonte18 = pyxel.Font("/home/hacdan/Documents/Linux/Programacao/Python/Projetos/Pyxel/FRACTALS_1.0/Assets/Fonts/helvB18.bdf")
        self.fonte24 = pyxel.Font("/home/hacdan/Documents/Linux/Programacao/Python/Projetos/Pyxel/FRACTALS_1.0/Assets/Fonts/helvB24.bdf")
        #declarando tilemap para decoracao da janela menu
        self.decoration = pyxel.tilemaps[0]

        #declarando e inicializando retangulos do menu (para colisao e display de mensagens)
        self.recTitulo = [80, 78, 228, 63, pyxel.COLOR_PURPLE]
        self.recFractal1 = [201, 221, 114, 42, pyxel.COLOR_YELLOW]
        self.recFractal2 = [201, 341, 114, 42, pyxel.COLOR_LIGHT_BLUE]
        self.recFractal3 = [201, 461, 114, 42, pyxel.COLOR_BROWN]
        self.recFractal4 = [201, 581, 114, 42, pyxel.COLOR_GRAY]
        self.recSair = [490, 556, 280, 67, pyxel.COLOR_RED]
        self.recInfo = [420, 50, 420, 460, pyxel.COLOR_GRAY]
        #self.retangulos = [self.recTitulo, self.recFractal1, self.recFractal2, self.recFractal3, self.recFractal4, self.recSair, self.recInfo]
        #declarando flags de controle das opcoes do menu
        self.mouseOnFrac1 = False
        self.mouseOnFrac2 = False
        self.mouseOnFrac3 = False
        self.mouseOnFrac4 = False
        self.mouseOnSair = False
        self.mouseOnInfo = False

    def update (self, game):
        #checando se o usuario esta com o mouse em cima de alguma das opcoes do menu
        if (utilities.checkPointOnRec(pyxel.mouse_x, pyxel.mouse_y, self.recFractal1[0], self.recFractal1[1], self.recFractal1[2], self.recFractal1[3])):
            self.mouseOnFrac1 = True
        elif (utilities.checkPointOnRec(pyxel.mouse_x, pyxel.mouse_y, self.recFractal2[0], self.recFractal2[1], self.recFractal2[2], self.recFractal2[3])):
            self.mouseOnFrac2 = True
        elif (utilities.checkPointOnRec(pyxel.mouse_x, pyxel.mouse_y, self.recFractal3[0], self.recFractal3[1], self.recFractal3[2], self.recFractal3[3])):
            self.mouseOnFrac3 = True
        elif (utilities.checkPointOnRec(pyxel.mouse_x, pyxel.mouse_y, self.recFractal4[0], self.recFractal4[1], self.recFractal4[2], self.recFractal4[3])):
            self.mouseOnFrac4 = True
        elif (utilities.checkPointOnRec(pyxel.mouse_x, pyxel.mouse_y, self.recSair[0], self.recSair[1], self.recSair[2], self.recSair[3])):
            self.mouseOnSair = True
        elif (utilities.checkPointOnRec(pyxel.mouse_x, pyxel.mouse_y, self.recInfo[0], self.recInfo[1], self.recInfo[2], self.recInfo[3])):
            self.mouseOnInfo = True
        else:
            self.mouseOnFrac1 = False
            self.mouseOnFrac2 = False
            self.mouseOnFrac3 = False
            self.mouseOnFrac4 = False
            self.mouseOnSair = False
            self.mouseOnInfo = False
        
        #realizando opcoes de acordo com o clique do usuario
        if (pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT, hold=30)):
            if (self.mouseOnFrac1):
                #executando arquivo do fractal de Sierpinski
                return "fractal1"
            elif (self.mouseOnFrac2):
                #executando arquivo do fractal de Koch
                return "fractal2"
            elif (self.mouseOnSair):
                #finalizando execucao e fechando janela
                pyxel.quit()

    def draw(self, game):
        pyxel.cls(0) #limpando janela
        #desenhando tilemap
        utilities.draw_tilemapItens(pyxel, self.decoration, sprite_bank=0, LARGURA=37, ALTURA=29, TAMANHO=8, ESCALA=3)
        #desenhando menu (frases)
        pyxel.text(self.recTitulo[0]+10, self.recTitulo[1]+5, "FRACTALS 1.0", pyxel.COLOR_WHITE, self.fonte24)
        pyxel.text(self.recFractal1[0]+18, self.recFractal1[1]+10, "Sierpinski", pyxel.COLOR_ORANGE, self.fonte16)
        pyxel.text(self.recFractal2[0]+22, self.recFractal2[1]-1, "Koch", pyxel.COLOR_CYAN, self.fonte24)
        pyxel.text(self.recSair[0]+35, self.recSair[1]+10, "EXIT THE APP", pyxel.COLOR_RED, self.fonte24)
        
        #desenhando contorno nos botoes do menu caso o mouse esteja em cima deles
        if (self.mouseOnFrac1):
            pyxel.rectb(self.recFractal1[0], self.recFractal1[1], self.recFractal1[2], self.recFractal1[3], self.recFractal1[4])
        elif (self.mouseOnFrac2):
            pyxel.rectb(self.recFractal2[0], self.recFractal2[1], self.recFractal2[2], self.recFractal2[3], self.recFractal2[4])
        elif (self.mouseOnFrac3):
            pyxel.rectb(self.recFractal3[0], self.recFractal3[1], self.recFractal3[2], self.recFractal3[3], self.recFractal3[4])
        elif (self.mouseOnFrac4):
            pyxel.rectb(self.recFractal4[0], self.recFractal4[1], self.recFractal4[2], self.recFractal4[3], self.recFractal4[4])
        elif (self.mouseOnSair):
            pyxel.rectb(self.recSair[0], self.recSair[1], self.recSair[2], self.recSair[3], self.recSair[4])
        elif (self.mouseOnInfo):
            pyxel.rectb(self.recInfo[0], self.recInfo[1], self.recInfo[2], self.recInfo[3], self.recInfo[4])
        '''
        #desenhando retangulos
        for item in self.retangulos:
            pyxel.rect(item[0], item[1], item[2], item[3], item[4])
        '''