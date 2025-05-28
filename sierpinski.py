'''

    PROGRAMA AUXILIAR RESPONSAVEL POR MOSTRAR O MENU INICIAL DO JOGO SNAKE 2.0

    -> Conta com tres opcoes basicas:

    1. Jogar (inicia a fase 1)
    2. Tutorial (carrega janela Tutorial)
    3. Sair (finaliza o jogo)
'''
from fractals import State
from models import utilities
import pyxel
import random

#CODIGO PRINCIPAL
class Sierpinski(State):

    def onEnter(self, game):
        #inicializando janela
        pyxel.mouse(True)
        #carregando fonte de texto
        self.fonte5 = pyxel.Font("/home/hacdan/Documents/Linux/Programacao/Python/Projetos/Pyxel/FRACTALS_1.0/Assets/Fonts/5x8.bdf")
        self.fonte8 = pyxel.Font("/home/hacdan/Documents/Linux/Programacao/Python/Projetos/Pyxel/FRACTALS_1.0/Assets/Fonts/VictoriaBold-8.bdf")
        self.fonte16 = pyxel.Font("/home/hacdan/Documents/Linux/Programacao/Python/Projetos/Pyxel/FRACTALS_1.0/Assets/Fonts/b16_b.bdf")
        self.fonte18 = pyxel.Font("/home/hacdan/Documents/Linux/Programacao/Python/Projetos/Pyxel/FRACTALS_1.0/Assets/Fonts/helvB18.bdf")
        self.fonte24 = pyxel.Font("/home/hacdan/Documents/Linux/Programacao/Python/Projetos/Pyxel/FRACTALS_1.0/Assets/Fonts/helvB24.bdf")

        #declarando valores iniciais do fractal
        self.iterations = 100 #numero de passos a serem realizados para gerar o fractal
        self.origem = (550, 350) #ponto (0,0) do plano cartesiano com base nas dimensoes da tela
        #p1 = (0, 319.61), p2 = (-300, -200), p3 = (300, -200) -> TRIANGULO EQUILATERO INICIAL
        self.pontosIniciais = [ (self.origem[0], self.origem[1]-319.61), 
                       (self.origem[0]-300, self.origem[1]+200), 
                       (self.origem[0]+300, self.origem[1]+200)]
        self.pontos = [] #lista de pontos a serem gerados
        #serao usados posteriormente para geracao dos outros pontos
        self.i = -1
        self.j = -1
        #flag de controle para saber o nivel de zoom da aplicacao
        self.zoom = 1 #setado para iniciar em x1 (todo o plano cartesiano e seus 4 quadrantes)

        #declarando retangulos do menu (para efeitos de moldura e fundo)
        self.recMenu = (0, 0, 200, pyxel.height, pyxel.COLOR_GRAY)
        self.recConfig = (15, 15, 170, 50, pyxel.COLOR_BLACK)
        self.recTitulo = (5, 5, 190, 100, pyxel.COLOR_BLACK)
        self.recValorN = (80, 200, 40, 20, pyxel.COLOR_WHITE)
        self.recZoom = (25, 240, 150, 40, pyxel.COLOR_BLACK)
        #declarando conjunto de retangulos (suas dimensoes) que sera utilizados para o submenu de zoom in-out (setados em False para mouse e False para clique)
        self.recQuadrantes = [[30, 300, 140, 140, False, False], #todo o plano (x1)
                              [30, 300, 70, 70, False, False], [100, 300, 70, 70, False, False], #Q1, Q2, Q3 e Q4 (x4)
                              [30, 370, 70, 70, False, False], [100, 370, 70, 70, False, False],
                              [30, 300, 35, 35, False, False], [65, 300, 35, 35, False, False], #Q1-Q2 (x8)
                              [100, 300, 35, 35, False, False], [135, 300, 35, 35, False, False],
                              [30, 335, 35, 35, False, False], [65, 335, 35, 35, False, False],
                              [100, 335, 35, 35, False, False], [135, 335, 35, 35, False, False],
                              [30, 370, 35, 35, False, False], [65, 370, 35, 35, False, False], #Q3-Q4 (x8)
                              [100, 370, 35, 35, False, False], [135, 370, 35, 35, False, False],
                              [30, 405, 35, 35, False, False], [65, 405, 35, 35, False, False],
                              [100, 405, 35, 35, False, False], [135, 405, 35, 35, False, False]]
        #declarando botoes do menu de config
        self.buttonRun = (20, 120, 60, 60, pyxel.COLOR_GREEN)
        self.buttonClean = (120, 120, 60, 60, pyxel.COLOR_YELLOW)
        self.buttonNplus1 = (125, 200, 20, 20, pyxel.COLOR_LIGHT_BLUE)
        self.buttonNplus10 = (150, 200, 20, 20, pyxel.COLOR_LIGHT_BLUE)
        self.buttonNplus50 = (175, 200, 20, 20, pyxel.COLOR_LIGHT_BLUE)
        self.buttonNminus1 = (55, 200, 20, 20, pyxel.COLOR_PEACH)
        self.buttonNminus10 = (30, 200, 20, 20, pyxel.COLOR_PEACH)
        self.buttonNminus50 = (5, 200, 20, 20, pyxel.COLOR_PEACH)
        self.button1x = (30, 460, 40, 40, pyxel.COLOR_NAVY)
        self.button4x = (80,460, 40, 40, pyxel.COLOR_NAVY)
        self.button8x = (130, 460, 40, 40, pyxel.COLOR_NAVY)
        #declarando flag de controle dos botoes
        self.mouseOnRun = False
        self.mouseOnClear = False
        self.mouseOnPlus1 = False
        self.mouseOnPlus10 = False
        self.mouseOnPlus50 = False
        self.mouseOnMinus1 = False
        self.mouseOnMinus10 = False
        self.mouseOnMinus50 = False
        self.mouseOn1x = False
        self.mouseOn4x = False
        self.mouseOn8x = False


    def update(self, game):
        #checando cursor do mouse esta em cima de algum dos botoes do menu
        if (utilities.checkPointOnRec(pyxel.mouse_x, pyxel.mouse_y, self.buttonRun[0], self.buttonRun[1], self.buttonRun[2], self.buttonRun[3])):
            self.mouseOnRun = True
        elif (utilities.checkPointOnRec(pyxel.mouse_x, pyxel.mouse_y, self.buttonClean[0], self.buttonClean[1], self.buttonClean[2], self.buttonClean[3])):
            self.mouseOnClear = True
        elif (utilities.checkPointOnRec(pyxel.mouse_x, pyxel.mouse_y, self.buttonNplus1[0], self.buttonNplus1[1], self.buttonNplus1[2], self.buttonNplus1[3])):
            self.mouseOnPlus1 = True
        elif (utilities.checkPointOnRec(pyxel.mouse_x, pyxel.mouse_y, self.buttonNplus10[0], self.buttonNplus10[1], self.buttonNplus10[2], self.buttonNplus10[3])):
            self.mouseOnPlus10 = True
        elif (utilities.checkPointOnRec(pyxel.mouse_x, pyxel.mouse_y, self.buttonNplus50[0], self.buttonNplus50[1], self.buttonNplus50[2], self.buttonNplus50[3])):
            self.mouseOnPlus50 = True
        elif (utilities.checkPointOnRec(pyxel.mouse_x, pyxel.mouse_y, self.buttonNminus1[0], self.buttonNminus1[1], self.buttonNminus1[2], self.buttonNminus1[3])):
            self.mouseOnMinus1 = True
        elif (utilities.checkPointOnRec(pyxel.mouse_x, pyxel.mouse_y, self.buttonNminus10[0], self.buttonNminus10[1], self.buttonNminus10[2], self.buttonNminus10[3])):
            self.mouseOnMinus10 = True
        elif (utilities.checkPointOnRec(pyxel.mouse_x, pyxel.mouse_y, self.buttonNminus50[0], self.buttonNminus50[1], self.buttonNminus50[2], self.buttonNminus50[3])):
            self.mouseOnMinus50 = True
        elif (utilities.checkPointOnRec(pyxel.mouse_x, pyxel.mouse_y, self.button1x[0], self.button1x[1], self.button1x[2], self.button1x[3])):
            self.mouseOn1x = True
            self.mouseOn4x = False
            self.mouseOn8x = False
        elif (utilities.checkPointOnRec(pyxel.mouse_x, pyxel.mouse_y, self.button4x[0], self.button4x[1], self.button4x[2], self.button4x[3])):
            self.mouseOn4x = True
            self.mouseOn1x = False
            self.mouseOn8x = False
        elif (utilities.checkPointOnRec(pyxel.mouse_x, pyxel.mouse_y, self.button8x[0], self.button8x[1], self.button8x[2], self.button8x[3])):
            self.mouseOn8x = True
            self.mouseOn1x = False
            self.mouseOn4x = False
        else:
            self.mouseOnRun = False
            self.mouseOnClear = False
            self.mouseOnPlus1 = False
            self.mouseOnPlus10 = False
            self.mouseOnPlus50 = False
            self.mouseOnMinus1 = False
            self.mouseOnMinus10 = False
            self.mouseOnMinus50 = False
        #checando a posicao do mouse para ver se esta em cima de algum dos quadrantes (de acordo com o zoom)
        if (self.zoom == 1):
            if (utilities.checkPointOnRec(pyxel.mouse_x, pyxel.mouse_y, self.recQuadrantes[0][0], self.recQuadrantes[0][1], self.recQuadrantes[0][2], self.recQuadrantes[0][3])):
                self.recQuadrantes[0][4] = True #ativando flag para sinalizar que o mouse esta em cima desse quadrante
            else:
                self.recQuadrantes[0][4] = False
        elif (self.zoom == 4):
            for i in range(1, 5):
                if (utilities.checkPointOnRec(pyxel.mouse_x, pyxel.mouse_y, self.recQuadrantes[i][0], self.recQuadrantes[i][1], self.recQuadrantes[i][2], self.recQuadrantes[i][3])):
                    self.recQuadrantes[i][4] = True #ativando flag para sinalizar que o mouse esta em cima desse quadrante
                else:
                    self.recQuadrantes[i][4] = False 
        elif (self.zoom == 8):
            for i in range(5, 21):
                if (utilities.checkPointOnRec(pyxel.mouse_x, pyxel.mouse_y, self.recQuadrantes[i][0], self.recQuadrantes[i][1], self.recQuadrantes[i][2], self.recQuadrantes[i][3])):
                    self.recQuadrantes[i][4] = True #ativando flag para sinalizar que o mouse esta em cima desse quadrante
                else:
                    self.recQuadrantes[i][4] = False 
        #verificando se ocorreu clique do mouse, e se sim, se foi em algum dos botoes ou quadrantes
        if (pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT, hold=10)):
            #checando clique em um dos quadrantes do submenu ZOOM quando o mouse estiver por la, True se ocorreu clique...
            if (utilities.checkPointOnRec(pyxel.mouse_x, pyxel.mouse_y, self.recQuadrantes[0][0], self.recQuadrantes[0][1], self.recQuadrantes[0][2], self.recQuadrantes[0][3])):
                for quadrante in self.recQuadrantes:
                    if (quadrante[4]):
                        quadrante[5] = True #ativando flag para desenhar conteudo desse quadrante em especifico
                    else:
                        quadrante[5] = False
            #checando clique nos outros botoes
            if (self.mouseOnRun):
                #gerando N pontos do triangulo de sierpinski de acordo com os pontos iniciais
                for N in range(self.iterations):
                    #o primeiro ponto aleatorio de referencia sera a origem
                    if (N == 0 and len(self.pontos) == 0):
                        i = -1
                    else:
                        i = random.randint(0, len(self.pontos)-1) #aleatoriamente pegando ponto 1 do conjunto de pontos
                    j = random.randint(0, 2) #aleatoriamente pegando ponto 2 do conjunto de pontos Iniciais
                    #calculando ponto medio entre os 2 pontos alatoriamente escolhido no conjunto de pontos ja gerados
                    if (N == 0 and len(self.pontos) == 0):
                        x = (self.origem[0]+self.pontosIniciais[j][0])/2 #coordenada X do novo ponto
                        y = (self.origem[1]+self.pontosIniciais[j][1])/2 #coordenada Y do novo ponto
                    else:
                        x = (self.pontos[i][0]+self.pontosIniciais[j][0])/2 #coordenada X do novo ponto
                        y = (self.pontos[i][1]+self.pontosIniciais[j][1])/2 #coordenada Y do novo ponto
                    self.pontos.append((x, y)) #adicionando novo ponto
            elif (self.mouseOnClear):
                #apagando todos os pontos gerados, exceto os 3 iniciais
                if ( len(self.pontos) > 3):
                    for i in range(len(self.pontos)):
                        self.pontos.pop()
            elif (self.mouseOnPlus1):
                #acrescentando +1 no valor da iteracoes
                self.iterations += 1
            elif (self.mouseOnPlus10):
                #acrescentando +10 no valor das iteracoes
                self.iterations += 10
            elif (self.mouseOnPlus50):
                #acrescentando +50 no valor das iteracoes
                self.iterations += 50
            elif (self.mouseOnMinus1):
                #reduzindo -1 no valor da iteracoes, a depender do valor atual
                if (self.iterations > 1):
                    self.iterations -= 1
            elif (self.mouseOnMinus10):
                #reduzindo -10 no valor da iteracoes, a depender do valor atual
                if (self.iterations > 10):
                    self.iterations -= 10
                else:
                    self.iterations = 1 #menor valor possivel
            elif (self.mouseOnMinus50):
                #reduzindo -50 no valor da iteracoes, a depender do valor atual
                if (self.iterations > 50):
                    self.iterations -= 50
                else:
                    self.iterations = 1 #menor valor possivel
            elif (self.mouseOn1x):
                self.zoom = 1 #setando zoom da aplicacao para x1
            elif (self.mouseOn4x):
                self.zoom = 4 #setando zoom da aplicacao para x4
            elif (self.mouseOn8x):
                self.zoom = 8 #setando zoom da aplicacao para x8

    def draw(self, game):
        pyxel.cls(0) #limpando tela
        #desenhando detalhes do menu (molduras, textos e botoes)
        pyxel.rect(self.recMenu[0], self.recMenu[1], self.recMenu[2], self.recMenu[3], self.recMenu[4]) #fundo cinza do retangulo menu
        pyxel.rectb(self.recConfig[0], self.recConfig[1], self.recConfig[2], self.recConfig[3], self.recConfig[4]) #moldura do texto CONFIG
        pyxel.text(self.recConfig[0]+25, self.recConfig[1]+2, "CONFIG", pyxel.COLOR_WHITE, self.fonte24) #texto CONFIG
        pyxel.text(self.recTitulo[0]+7, self.recTitulo[1]+70, "Triangle of Sierpinski", pyxel.COLOR_WHITE, self.fonte16) #texto do nome do fractal
        pyxel.rectb(self.recTitulo[0], self.recTitulo[1], self.recTitulo[2], self.recTitulo[3], self.recTitulo[4]) #moldura do titulo
        pyxel.rect(self.buttonRun[0], self.buttonRun[1], self.buttonRun[2], self.buttonRun[3], self.buttonRun[4]) #fundo do botao RUN
        pyxel.text(self.buttonRun[0]+18, self.buttonRun[1]+20, "RUN", pyxel.COLOR_WHITE, self.fonte16) #texto do botao RUN
        pyxel.rect(self.buttonClean[0], self.buttonClean[1], self.buttonClean[2], self.buttonClean[3], self.buttonClean[4]) #fundo do botao CLEAR
        pyxel.text(self.buttonClean[0]+10, self.buttonClean[1]+20, "CLEAR", pyxel.COLOR_WHITE, self.fonte16) #texto do botao CLEAR
        pyxel.rect(self.recValorN[0], self.recValorN[1], self.recValorN[2], self.recValorN[3], self.recValorN[4]) #fundo da janela do valor N
        pyxel.rectb(self.recValorN[0], self.recValorN[1], self.recValorN[2], self.recValorN[3], self.recValorN[4]) #moldura da janela do valor N
        if (self.iterations >= 10000):
            pyxel.text(self.recValorN[0]+5, self.recValorN[1]+2, str(int(self.iterations/1000))+"k", pyxel.COLOR_BLACK, self.fonte16) #texto do valor N 
        else:
            pyxel.text(self.recValorN[0]+5, self.recValorN[1]+2, str(self.iterations), pyxel.COLOR_BLACK, self.fonte16) #texto do valor N 
        pyxel.rect(self.buttonNplus1[0], self.buttonNplus1[1], self.buttonNplus1[2], self.buttonNplus1[3], self.buttonNplus1[4]) #fundo do botao +1
        pyxel.text(self.buttonNplus1[0]+1, self.buttonNplus1[1]+6, "+1", pyxel.COLOR_ORANGE, self.fonte8) #texto do botao +1
        pyxel.rect(self.buttonNplus10[0], self.buttonNplus10[1], self.buttonNplus10[2], self.buttonNplus10[3], self.buttonNplus10[4]) #fundo do botao +10
        pyxel.text(self.buttonNplus10[0]+3, self.buttonNplus10[1]+5, "+10", pyxel.COLOR_ORANGE, self.fonte5) #texto do botao +10
        pyxel.rect(self.buttonNplus50[0], self.buttonNplus50[1], self.buttonNplus50[2], self.buttonNplus50[3], self.buttonNplus50[4]) #fundo do botao +50
        pyxel.text(self.buttonNplus50[0]+3, self.buttonNplus50[1]+5, "+50", pyxel.COLOR_ORANGE, self.fonte5) #texto do botao +50
        pyxel.rect(self.buttonNminus1[0], self.buttonNminus1[1], self.buttonNminus1[2], self.buttonNminus1[3], self.buttonNminus1[4]) #fundo do botao -1
        pyxel.text(self.buttonNminus1[0]+1, self.buttonNminus1[1]+6, "-1", pyxel.COLOR_ORANGE, self.fonte8) #texto do botao -1
        pyxel.rect(self.buttonNminus10[0], self.buttonNminus10[1], self.buttonNminus10[2], self.buttonNminus10[3], self.buttonNminus10[4]) #fundo do botao -10
        pyxel.text(self.buttonNminus10[0]+3, self.buttonNminus10[1]+5, "-10", pyxel.COLOR_ORANGE, self.fonte5) #texto do botao -10
        pyxel.rect(self.buttonNminus50[0], self.buttonNminus50[1], self.buttonNminus50[2], self.buttonNminus50[3], self.buttonNminus50[4]) #fundo do botao -50
        pyxel.text(self.buttonNminus50[0]+3, self.buttonNminus50[1]+5, "-50", pyxel.COLOR_ORANGE, self.fonte5) #texto do botao -50
        pyxel.rectb(self.recZoom[0], self.recZoom[1], self.recZoom[2], self.recZoom[3], self.recZoom[4]) #moldura do texto ZOOM
        pyxel.text(self.recZoom[0]+40, self.recZoom[1]+2, "ZOOM", pyxel.COLOR_WHITE, self.fonte18) #texto ZOOM
        pyxel.rect(self.button1x[0], self.button1x[1], self.button1x[2], self.button1x[3], self.button1x[4]) #fundo do botao ZOOM x1
        pyxel.text(self.button1x[0]+14, self.button1x[1]+10, "x1", pyxel.COLOR_ORANGE, self.fonte16) #texto do botao ZOOM x1
        pyxel.rect(self.button4x[0], self.button4x[1], self.button4x[2], self.button4x[3], self.button4x[4]) #fundo do botao ZOOM x4
        pyxel.text(self.button4x[0]+14, self.button4x[1]+10, "x4", pyxel.COLOR_ORANGE, self.fonte16) #texto do botao ZOOM x4
        pyxel.rect(self.button8x[0], self.button8x[1], self.button8x[2], self.button8x[3], self.button8x[4]) #fundo do botao ZOOM x8
        pyxel.text(self.button8x[0]+14, self.button8x[1]+10, "x8", pyxel.COLOR_ORANGE, self.fonte16) #texto do botao ZOOM x8
        #desenhando submenu do ZOOM IN-OUT de acordo com o zoom selecionado (x1, x4, x8)
        if (self.zoom == 1):
            #apenas desenhando o primeiro retangulo (que ira representar td o plano cartesiano e seus 4 quadrantes)
            pyxel.rect(self.recQuadrantes[0][0], self.recQuadrantes[0][1], self.recQuadrantes[0][2], self.recQuadrantes[0][3], self.recQuadrantes[0][4])
        elif (self.zoom == 4):
            for i in range(1, 5):
                #desenhando 4 retangulos menores (que irao representar os quadrantes Q1, Q2, 23 e Q4)
                pyxel.rect(self.recQuadrantes[i][0], self.recQuadrantes[i][1], self.recQuadrantes[i][2], self.recQuadrantes[i][3], self.recQuadrantes[i][4])
        elif (self.zoom == 8):
            for i in range(5, 21):
                #desenhando 16 retangulos menores (que irao representar os quadrantes Q1, Q2, 23 e Q4 divididos em 4 quadrantes menores cada)
                pyxel.rect(self.recQuadrantes[i][0], self.recQuadrantes[i][1], self.recQuadrantes[i][2], self.recQuadrantes[i][3], self.recQuadrantes[i][4])
        #desenhando efeito de destaque nos quadrantes ao passar o mouse em cima
        for quadrante in self.recQuadrantes:
                if (quadrante[4]):
                    pyxel.rectb(quadrante[0], quadrante[1], quadrante[2], quadrante[3], pyxel.COLOR_ORANGE)
        #desenhando efeito de destaque nos botoes ao passar o mouse em cima
        if (self.mouseOnRun):
            pyxel.rectb(self.buttonRun[0], self.buttonRun[1], self.buttonRun[2], self.buttonRun[3], pyxel.COLOR_WHITE)
        elif (self.mouseOnClear):
            pyxel.rectb(self.buttonClean[0], self.buttonClean[1], self.buttonClean[2], self.buttonClean[3], pyxel.COLOR_WHITE)
        elif (self.mouseOnPlus1):
            pyxel.rectb(self.buttonNplus1[0], self.buttonNplus1[1], self.buttonNplus1[2], self.buttonNplus1[3], pyxel.COLOR_WHITE)
        elif (self.mouseOnPlus10):
            pyxel.rectb(self.buttonNplus10[0], self.buttonNplus10[1], self.buttonNplus10[2], self.buttonNplus10[3], pyxel.COLOR_WHITE)
        elif (self.mouseOnPlus50):
            pyxel.rectb(self.buttonNplus50[0], self.buttonNplus50[1], self.buttonNplus50[2], self.buttonNplus50[3], pyxel.COLOR_WHITE)
        elif (self.mouseOnMinus1):
            pyxel.rectb(self.buttonNminus1[0], self.buttonNminus1[1], self.buttonNminus1[2], self.buttonNminus1[3], pyxel.COLOR_WHITE)
        elif (self.mouseOnMinus10):
            pyxel.rectb(self.buttonNminus10[0], self.buttonNminus10[1], self.buttonNminus10[2], self.buttonNminus10[3], pyxel.COLOR_WHITE)
        elif (self.mouseOnMinus50):
            pyxel.rectb(self.buttonNminus50[0], self.buttonNminus50[1], self.buttonNminus50[2], self.buttonNminus50[3], pyxel.COLOR_WHITE)
        #verificando qual porcao do plano desenhar de acordo com o zoom e quadrante escolhido
        if (self.zoom == 1):
            #desenhando borda do botao x1 para demonstrar qual zoom esta selecionado
            pyxel.rectb(self.button1x[0], self.button1x[1], self.button1x[2], self.button1x[3], pyxel.COLOR_ORANGE)
            #desenhando plano cartesiano (x1)
            utilities.drawCartesianPlan(200, 0, 700, 700, 5)
            #desenhando pontos iniciais (como circulos de raio=5)
            for ponto in self.pontosIniciais:
                pyxel.circ(ponto[0], ponto[1], 5, pyxel.COLOR_PURPLE)
            #desenhando o resto dos pontos gerados (como circulos de raio = 1)
            for ponto in self.pontos:
                pyxel.circ(ponto[0], ponto[1], 1, pyxel.COLOR_ORANGE)
        elif (self.zoom == 4):
            #desenhando borda do botao x2 para demonstrar qual zoom esta selecionado
            pyxel.rectb(self.button4x[0], self.button4x[1], self.button4x[2], self.button4x[3], pyxel.COLOR_ORANGE)
            #procurando qual quadrante do zoom x4 foi escolhido
            for i in range(1, 5):
                if (self.recQuadrantes[i][5] == True and i == 1):
                    #desenhando os pontos gerados pertencentes ao Q1(como circulos de raio = 1)
                    for ponto in self.pontos:
                        if (utilities.checkPointOnRec(ponto[0], ponto[1], 200, 0, 350, 350)):
                            #calculando variacoes no deslocamento dos pontos para (x,y)
                            Dx = (self.origem[0]-ponto[0])*2
                            Dy = (self.origem[1]-ponto[1])*2
                            OrigemQ1 = [900, 700]
                            pyxel.circ(OrigemQ1[0]-Dx, OrigemQ1[1]-Dy, 1, pyxel.COLOR_ORANGE)
                elif (self.recQuadrantes[i][5] == True and i == 2):
                    #desenhando os pontos gerados pertencentes ao Q2(como circulos de raio = 1)
                    for ponto in self.pontos:
                        if (utilities.checkPointOnRec(ponto[0], ponto[1], 550, 0, 350, 350)):
                            #calculando variacoes no deslocamento dos pontos para (x,y)
                            Dx = (ponto[0]-self.origem[0])*2
                            Dy = (self.origem[1]-ponto[1])*2
                            OrigemQ2 = [200, 700]
                            pyxel.circ(OrigemQ2[0]+Dx, OrigemQ2[1]-Dy, 1, pyxel.COLOR_ORANGE)
                elif (self.recQuadrantes[i][5] == True and i == 3):
                    #desenhando os pontos gerados pertencentes ao Q3(como circulos de raio = 1)
                    for ponto in self.pontos:
                        if (utilities.checkPointOnRec(ponto[0], ponto[1], 200, 350, 350, 350)):
                            #calculando variacoes no deslocamento dos pontos para (x,y)
                            Dx = (self.origem[0]-ponto[0])*2
                            Dy = (ponto[1]-self.origem[1])*2
                            OrigemQ3 = [900, 0]
                            pyxel.circ(OrigemQ3[0]-Dx, OrigemQ3[1]+Dy, 1, pyxel.COLOR_ORANGE)
                elif (self.recQuadrantes[i][5] == True and i == 4):
                    #desenhando os pontos gerados pertencentes ao Q4(como circulos de raio = 1)
                    for ponto in self.pontos:
                        if (utilities.checkPointOnRec(ponto[0], ponto[1], 550, 350, 350, 350)):
                            #calculando variacoes no deslocamento dos pontos para (x,y)
                            Dx = (ponto[0]-self.origem[0])*2
                            Dy = (ponto[1]-self.origem[1])*2
                            OrigemQ4 = [200, 0]
                            pyxel.circ(OrigemQ4[0]+Dx, OrigemQ4[1]+Dy, 1, pyxel.COLOR_ORANGE)
        elif (self.zoom == 8):
            #desenhando borda do botao x4 para demonstrar qual zoom esta selecionado
            pyxel.rectb(self.button8x[0], self.button8x[1], self.button8x[2], self.button8x[3], pyxel.COLOR_ORANGE)
            #procurando qual quadrante do zoom x8 foi escolhido
            for i in range(5, 21):
                if (self.recQuadrantes[i][5] == True and i == 5):
                    #desenhando os pontos gerados pertencentes ao Q1(como circulos de raio = 1)
                    for ponto in self.pontos:
                        if (utilities.checkPointOnRec(ponto[0], ponto[1], 200, 0, 175, 175)):
                            #calculando variacoes no deslocamento dos pontos para (x,y)
                            Dx = ((self.origem[0]-175)-ponto[0])*4
                            Dy = ((self.origem[1]-175)-ponto[1])*4
                            OrigemQ1 = [900, 700]
                            pyxel.circ(OrigemQ1[0]-Dx, OrigemQ1[1]-Dy, 1, pyxel.COLOR_ORANGE)
                elif (self.recQuadrantes[i][5] == True and i == 6):
                    #desenhando os pontos gerados pertencentes ao Q1(como circulos de raio = 1)
                    for ponto in self.pontos:
                        if (utilities.checkPointOnRec(ponto[0], ponto[1], 375, 0, 175, 175)):
                            #calculando variacoes no deslocamento dos pontos para (x,y)
                            Dx = (self.origem[0]-ponto[0])*4
                            Dy = ((self.origem[1]-175)-ponto[1])*4
                            OrigemQ1 = [900, 700]
                            pyxel.circ(OrigemQ1[0]-Dx, OrigemQ1[1]-Dy, 1, pyxel.COLOR_ORANGE)
                elif (self.recQuadrantes[i][5] == True and i == 9):
                    #desenhando os pontos gerados pertencentes ao Q1(como circulos de raio = 1)
                    for ponto in self.pontos:
                        if (utilities.checkPointOnRec(ponto[0], ponto[1], 200, 175, 175, 175)):
                            #calculando variacoes no deslocamento dos pontos para (x,y)
                            Dx = ((self.origem[0]-175)-ponto[0])*4
                            Dy = (self.origem[1]-ponto[1])*4
                            OrigemQ1 = [900, 700]
                            pyxel.circ(OrigemQ1[0]-Dx, OrigemQ1[1]-Dy, 1, pyxel.COLOR_ORANGE)
                elif (self.recQuadrantes[i][5] == True and i == 10):
                    #desenhando os pontos gerados pertencentes ao Q1(como circulos de raio = 1)
                    for ponto in self.pontos:
                        if (utilities.checkPointOnRec(ponto[0], ponto[1], 375, 175, 175, 175)):
                            #calculando variacoes no deslocamento dos pontos para (x,y)
                            Dx = (self.origem[0]-ponto[0])*4
                            Dy = (self.origem[1]-ponto[1])*4
                            OrigemQ1 = [900, 700]
                            pyxel.circ(OrigemQ1[0]-Dx, OrigemQ1[1]-Dy, 1, pyxel.COLOR_ORANGE)
                elif (self.recQuadrantes[i][5] == True and i == 7):
                    #desenhando os pontos gerados pertencentes ao Q2(como circulos de raio = 1)
                    for ponto in self.pontos:
                        if (utilities.checkPointOnRec(ponto[0], ponto[1], 550, 0, 175, 175)):
                            #calculando variacoes no deslocamento dos pontos para (x,y)
                            Dx = (ponto[0]-self.origem[0])*4
                            Dy = ((self.origem[1]-175)-ponto[1])*4
                            OrigemQ2 = [200, 700]
                            pyxel.circ(OrigemQ2[0]+Dx, OrigemQ2[1]-Dy, 1, pyxel.COLOR_ORANGE)
                elif (self.recQuadrantes[i][5] == True and i == 8):
                    #desenhando os pontos gerados pertencentes ao Q2(como circulos de raio = 1)
                    for ponto in self.pontos:
                        if (utilities.checkPointOnRec(ponto[0], ponto[1], 725, 0, 175, 175)):
                            #calculando variacoes no deslocamento dos pontos para (x,y)
                            Dx = (ponto[0]-(self.origem[0]+175))*4
                            Dy = ((self.origem[1]-175)-ponto[1])*4
                            OrigemQ2 = [200, 700]
                            pyxel.circ(OrigemQ2[0]+Dx, OrigemQ2[1]-Dy, 1, pyxel.COLOR_ORANGE)
                elif (self.recQuadrantes[i][5] == True and i == 11):
                    #desenhando os pontos gerados pertencentes ao Q2(como circulos de raio = 1)
                    for ponto in self.pontos:
                        if (utilities.checkPointOnRec(ponto[0], ponto[1], 550, 175, 175, 175)):
                            #calculando variacoes no deslocamento dos pontos para (x,y)
                            Dx = (ponto[0]-self.origem[0])*4
                            Dy = (self.origem[1]-ponto[1])*4
                            OrigemQ2 = [200, 700]
                            pyxel.circ(OrigemQ2[0]+Dx, OrigemQ2[1]-Dy, 1, pyxel.COLOR_ORANGE)
                elif (self.recQuadrantes[i][5] == True and i == 12):
                    #desenhando os pontos gerados pertencentes ao Q2(como circulos de raio = 1)
                    for ponto in self.pontos:
                        if (utilities.checkPointOnRec(ponto[0], ponto[1], 725, 175, 175, 175)):
                            #calculando variacoes no deslocamento dos pontos para (x,y)
                            Dx = (ponto[0]-(self.origem[0]+175))*4
                            Dy = (self.origem[1]-ponto[1])*4
                            OrigemQ2 = [200, 700]
                            pyxel.circ(OrigemQ2[0]+Dx, OrigemQ2[1]-Dy, 1, pyxel.COLOR_ORANGE)
                elif (self.recQuadrantes[i][5] == True and i == 13):
                    #desenhando os pontos gerados pertencentes ao Q3(como circulos de raio = 1)
                    for ponto in self.pontos:
                        if (utilities.checkPointOnRec(ponto[0], ponto[1], 200, 350, 175, 175)):
                            #calculando variacoes no deslocamento dos pontos para (x,y)
                            Dx = ((self.origem[0]-175)-ponto[0])*4
                            Dy = (ponto[1]-self.origem[1])*4
                            OrigemQ3 = [900, 0]
                            pyxel.circ(OrigemQ3[0]-Dx, OrigemQ3[1]+Dy, 1, pyxel.COLOR_ORANGE)
                elif (self.recQuadrantes[i][5] == True and i == 14):
                    #desenhando os pontos gerados pertencentes ao Q3(como circulos de raio = 1)
                    for ponto in self.pontos:
                        if (utilities.checkPointOnRec(ponto[0], ponto[1], 375, 350, 175, 175)):
                            #calculando variacoes no deslocamento dos pontos para (x,y)
                            Dx = (self.origem[0]-ponto[0])*4
                            Dy = (ponto[1]-self.origem[1])*4
                            OrigemQ3 = [900, 0]
                            pyxel.circ(OrigemQ3[0]-Dx, OrigemQ3[1]+Dy, 1, pyxel.COLOR_ORANGE)
                elif (self.recQuadrantes[i][5] == True and i == 17):
                    #desenhando os pontos gerados pertencentes ao Q3(como circulos de raio = 1)
                    for ponto in self.pontos:
                        if (utilities.checkPointOnRec(ponto[0], ponto[1], 200, 525, 175, 175)):
                            #calculando variacoes no deslocamento dos pontos para (x,y)
                            Dx = ((self.origem[0]-175)-ponto[0])*4
                            Dy = (ponto[1]-(self.origem[1]+175))*4
                            OrigemQ3 = [900, 0]
                            pyxel.circ(OrigemQ3[0]-Dx, OrigemQ3[1]+Dy, 1, pyxel.COLOR_ORANGE)
                elif (self.recQuadrantes[i][5] == True and i == 18):
                    #desenhando os pontos gerados pertencentes ao Q3(como circulos de raio = 1)
                    for ponto in self.pontos:
                        if (utilities.checkPointOnRec(ponto[0], ponto[1], 375, 525, 175, 175)):
                            #calculando variacoes no deslocamento dos pontos para (x,y)
                            Dx = (self.origem[0]-ponto[0])*4
                            Dy = (ponto[1]-(self.origem[1]+175))*4
                            OrigemQ3 = [900, 0]
                            pyxel.circ(OrigemQ3[0]-Dx, OrigemQ3[1]+Dy, 1, pyxel.COLOR_ORANGE)
                elif (self.recQuadrantes[i][5] == True and i == 15):
                    #desenhando os pontos gerados pertencentes ao Q4(como circulos de raio = 1)
                    for ponto in self.pontos:
                        if (utilities.checkPointOnRec(ponto[0], ponto[1], 550, 350, 175, 175)):
                            #calculando variacoes no deslocamento dos pontos para (x,y)
                            Dx = (ponto[0]-self.origem[0])*4
                            Dy = (ponto[1]-self.origem[1])*4
                            OrigemQ4 = [200, 0]
                            pyxel.circ(OrigemQ4[0]+Dx, OrigemQ4[1]+Dy, 1, pyxel.COLOR_ORANGE)
                elif (self.recQuadrantes[i][5] == True and i == 16):
                    #desenhando os pontos gerados pertencentes ao Q4(como circulos de raio = 1)
                    for ponto in self.pontos:
                        if (utilities.checkPointOnRec(ponto[0], ponto[1], 725, 350, 175, 175)):
                            #calculando variacoes no deslocamento dos pontos para (x,y)
                            Dx = (ponto[0]-(self.origem[0]+175))*4
                            Dy = (ponto[1]-self.origem[1])*4
                            OrigemQ4 = [200, 0]
                            pyxel.circ(OrigemQ4[0]+Dx, OrigemQ4[1]+Dy, 1, pyxel.COLOR_ORANGE)
                elif (self.recQuadrantes[i][5] == True and i == 19):
                    #desenhando os pontos gerados pertencentes ao Q4(como circulos de raio = 1)
                    for ponto in self.pontos:
                        if (utilities.checkPointOnRec(ponto[0], ponto[1], 550, 525, 175, 175)):
                            #calculando variacoes no deslocamento dos pontos para (x,y)
                            Dx = (ponto[0]-self.origem[0])*4
                            Dy = (ponto[1]-(self.origem[1]+175))*4
                            OrigemQ4 = [200, 0]
                            pyxel.circ(OrigemQ4[0]+Dx, OrigemQ4[1]+Dy, 1, pyxel.COLOR_ORANGE)
                elif (self.recQuadrantes[i][5] == True and i == 20):
                    #desenhando os pontos gerados pertencentes ao Q4(como circulos de raio = 1)
                    for ponto in self.pontos:
                        if (utilities.checkPointOnRec(ponto[0], ponto[1], 725, 525, 175, 175)):
                            #calculando variacoes no deslocamento dos pontos para (x,y)
                            Dx = (ponto[0]-(self.origem[0]+175))*4
                            Dy = (ponto[1]-(self.origem[1]+175))*4
                            OrigemQ4 = [200, 0]
                            pyxel.circ(OrigemQ4[0]+Dx, OrigemQ4[1]+Dy, 1, pyxel.COLOR_ORANGE)
