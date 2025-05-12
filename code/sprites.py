from settings import * 
from random import choice,uniform 

class Player(pygame.sprite.Sprite):
    def __init__(self,size,pos,colour,groups):
        super().__init__(groups)

        self.image=pygame.Surface(size,pygame.SRCALPHA)
        pygame.draw.rect(self.image,colour,pygame.FRect((0,0),size),0,4) # for making the sides rounded
        self.rect=self.image.get_frect(topleft=pos)
        self.old_rect=self.rect.copy()

        # direction
        self.direction=0
        self.speed=SPEED['player']
    
    def move(self,dt):
        self.rect.centery+=self.direction*self.speed*dt
        self.rect.top=0 if self.rect.top < 0 else self.rect.top
        self.rect.bottom=WINDOW_HEIGHT if self.rect.bottom > WINDOW_HEIGHT else self.rect.bottom

    def get_direction(self):
        keys=pygame.key.get_pressed()
        self.direction=int(keys[pygame.K_DOWN])-int(keys[pygame.K_UP])

    def update(self,dt):
        self.old_rect=self.rect.copy()
        self.get_direction()
        self.move(dt)
        

class Ball(pygame.sprite.Sprite):
    def __init__ (self,paddle_sprites,groups):
        super().__init__(groups)
        self.paddle_sprites=paddle_sprites
        self.image=pygame.Surface(SIZE['ball'],pygame.SRCALPHA)
        pygame.draw.circle(self.image,COLORS['ball'],(SIZE['ball'][0]/2,SIZE['ball'][1]/2),SIZE['ball'][0]/2) #for circle
        self.rect=self.image.get_frect(center=(WINDOW_WIDTH/2,WINDOW_HEIGHT/2))
        self.direction=pygame.Vector2(choice((1,-1)),uniform(0.7,0.8)*choice((-1,1)))
        self.old_rect=self.rect.copy()

    def move(self,dt):
        self.rect.x += SPEED['ball']*self.direction.x*dt
        self.collision('horizontal')
        self.rect.y += SPEED['ball']*self.direction.y*dt
        self.collision('vertical')

        if self.rect.bottom>WINDOW_HEIGHT or self.rect.top<0:
            self.direction.y*=-1
        elif self.rect.right>WINDOW_WIDTH or self.rect.left<0:
            self.direction.x*=-1
        
    def collision(self,direction):
        for sprite in self.paddle_sprites:
            if sprite.rect.colliderect(self.rect):
                if direction=='horizontal':
                    if self.rect.right >sprite.rect.left and self.old_rect.right<=sprite.old_rect.left:
                        self.rect.right=sprite.rect.left
                        self.direction.x*=-1
                    
                else :
                    if self.rect.bottom>=self.rect.top and self.old_rect.bottom<=sprite.old_rect.left:
                        self.rect.bottom=sprite.rect.top


    def update(self,dt):
        self.old_rect=self.rect.copy()
        self.move(dt)
        
            
         