import pygame as pg
from squad.config import *
from squad.sprites import *


class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.all_sprites = pg.sprite.Group()
        self.clock = pg.time.Clock()
        self.dt = self.clock.tick(FPS)

        print("Sprites", self.all_sprites)


        # player_1 placement
        for p1_coordinate in P1_PIECE_COORDINATES:
            Wall(self, p1_coordinate[0], p1_coordinate[1], player_no=1)

        # player_2 placement
        for p2_coordinate in P2_PIECE_COORDINATES:
            Wall(self, p2_coordinate[0], p2_coordinate[1], player_no=2)

        print("Sprites after", self.all_sprites)

        self.gameloop()

    def run(self):
        # game loop - set self.playing = False to end the game
        print("Game running")
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS)

            self.events()
            self.update()
            self.draw()

    def draw(self):
        # fill background
        self.screen.fill(BGCOLOR)
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()

    def events(self):

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False

            # example key event
            if event.type == pg.KEYDOWN:
               if event.key == pg.K_UP:
                   print("UP PRESSED")

            if event.type == pg.KEYDOWN:
               if event.key == pg.K_ESCAPE:
                   self.playing = False

    def gameloop(self):
        self.run()

        print("Game Over!")