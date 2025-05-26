import pyxel
from sierpinski import Sierpinski

class App:
    def __init__(self):
        pyxel.init(900, 700, "FRACTALS 1.0", fps=60)
        self.states = {
            "fractal1": Sierpinski()
        }
        self.currentState = self.states["fractal1"]
        self.currentState.onEnter(self)
        pyxel.run(self.update, self.draw)
    
    def changeState(self, stateName):
        self.currentState.onExit(self)
        self.currentState = self.states[stateName]
        self.currentState.onEnter(self)

    def update(self):
        nextState = self.currentState.update(self)
        if nextState:
            self.changeState(nextState)
    
    def draw(self):
        self.currentState.draw(self)
