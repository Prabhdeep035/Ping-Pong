import pygame
from settings import * 
from sprites import *

class Game:
    def __init__(self):
        pygame.init()
        self.display_surf=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        self.clock=pygame.time.Clock()
        pygame.display.set_caption('Pong')
        self.running=True

        # colour
        self.screen_colour=COLORS['bg']
        # self.paddle_colour=COLORS['paddle']
        self.paddle_shadow=COLORS['paddle shadow']
        self.ball_colour=COLORS['ball']
        self.ball_shadow=COLORS['ball shadow']

        #sprites
        self.all_sprites=pygame.sprite.Group()
        self.paddle_sprites=pygame.sprite.Group()

        self.player()
        self.ball()

    def player(self):
            self.paddle=Player(SIZE['paddle'],
                               POS['player'],   
                               COLORS['paddle'],
                               (self.all_sprites,
                                self.paddle_sprites))

    def ball(self):
            self.ball=Ball(self.paddle_sprites,
                           (self.all_sprites))

    def run(self):
        while (self.running):
            self.dt=self.clock.tick()/1000

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.running=False

            self.display_surf.fill(self.screen_colour)
            self.all_sprites.draw(self.display_surf)
            self.all_sprites.update(self.dt)
            pygame.display.update()
        pygame.quit()
if __name__=='__main__':
    game=Game()
    game.run()