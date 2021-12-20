import pygame as pg
from squad.config import *
from squad.sprites import *

import numpy as np
import math
from typing import *

class Game:
    def __init__(self) -> None:
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.all_sprites = pg.sprite.Group()
        self.clock = pg.time.Clock()
        self.dt = self.clock.tick(FPS)
        self.player1 = list()
        self.player2 = list()
        self.playing = False
        self.board = self.load_board()
        self.turn = [1,0]
        self.gameloop()

    def draw(self) -> NoReturn:
        # fill background
        self.screen.fill(BGCOLOR)
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

        self.display_sprites(self.board)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def update(self):
        # update portion of the game loop
        pass

    def events(self) -> NoReturn:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
            # example key event
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    print("UP PRESSED")
                    player_no, pawn_idx, loc_from, loc_to = self.decision()
                    self.update_board(player_no, pawn_idx, loc_from, loc_to)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.playing = False

    def run(self) -> NoReturn:
        # game loop - set self.playing = False to end the game
        print("Game running")
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def gameloop(self):
        self.run()
        print("Game Over!")

    def load_board(self) -> np.ndarray:
        board = np.zeros((7, 7), dtype=int)
        # player_1 placement
        for p1_coordinate in P1_PIECE_COORDINATES:
            board[p1_coordinate[0], p1_coordinate[1]] = 1
            self.player1.append(Pawn(p1_coordinate))
        # player_2 placement
        for p2_coordinate in P2_PIECE_COORDINATES:
            board[p2_coordinate[0], p2_coordinate[1]] = 2
            self.player2.append(Pawn(p2_coordinate))
        return board

    def display_sprites(self, board) -> NoReturn:
        # clear sprites
        self.all_sprites.empty()
        # set pieces sprites on scene
        for r in range(board.shape[0]):
            for c in range(board[r].shape[0]):
                territory_value = board[r, c]
                if territory_value == 1:
                    Pieces(self, c, r, player_no=1)
                elif territory_value == 2:
                    Pieces(self, c, r, player_no=2)

    def decision(self):
        player_no = 1
        pawn_idx = 1
        loc_from = self.player1[player_no].location
        loc_to = (loc_from[0], loc_from[1] + 1)
        return player_no, pawn_idx, loc_from, loc_to

    def update_board(self, player_no, pawn_idx, loc_from, loc_to):
        self.board[loc_from[0], loc_from[1]] = 0
        self.board[loc_to[0], loc_to[1]] = 1
        self.player1[player_no].location = loc_to

    def score(self) -> int:
        return 0
