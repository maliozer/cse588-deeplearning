import pygame as pg
from squad.config import *

from typing import Tuple

class Pieces(pg.sprite.Sprite):
    def __init__(self, game, x, y, player_no):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        # self.image = pg.Surface((TILESIZE, TILESIZE))
        if player_no == 1:
            image_path = "./src/images/circle.png"
        elif player_no == 2:
            image_path = "./src/images/triangle.png"
        else:
            raise "player_no must be given!"
        self.image = pg.image.load(image_path)
        self.image = pg.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Pawn:
    def __init__(self, initial_location: Tuple):
        assert type(initial_location) == tuple
        self.location = initial_location
        self.is_death = False
        self.is_moved = False

    def move(self, to_move: Tuple):
        assert type(to_move) == tuple
        self.location = to_move
