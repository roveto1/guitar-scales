import pygame as pg
import pygame_gui as pg_gui
import random
from settings import *

class Text():
    def __init__(self,txt,key,size) -> None:
        self.key = key
        self.font = pg.font.SysFont("Arial", size)
        self.color = BLACK
        if txt == self.key:
            self.color = RED
        self.txt = self.font.render(txt,1,self.color)