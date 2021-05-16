from pygame import *
class GameSprite(sprite.Sprite):
    def  __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y >0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y <400:
            self.rect.y += self.speed
        if keys_pressed[K_LEFT] and self.rect.x >0:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x <600:
            self.rect.x += self.speed
        
    
class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= 600:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self , color_1 , color_2 , color_3 , wall_x , wall_y , wall_width , wall_height):
        super().__init__()
        self.color_1=color_1
        self.color_2=color_2
        self.color_3=color_3
        self.width=wall_width
        self.height=wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect=self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x,self.rect.y))



window = display.set_mode((700,500))
display.set_caption("Лабиринт")
background = transform.scale(image.load("background.jpg"), (700,500))

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

hero = Player("hero.png",120,120,10)
cyborg= Enemy("cyborg.png",420,130,4)
treasure = GameSprite("treasure.png",600,400,10)
hgh = Wall(242, 144, 15,200,200,15,400)
# qqq = Wall(242, 144, 15,400,460,230,20)
ppp = Wall(242, 144, 15,400,460,20,23)
aaa = Wall(242, 150, 15,350,0,20,230)
sss = Wall(242, 150, 15,450,230,15,400)
game = True
Finish=False
while game:
    if not Finish:


        window.blit(background,(0,0))
        hero.reset()
        hero.update()
        cyborg.reset()
        treasure.reset()
        cyborg.update()
        hgh.draw_wall()
        # qqq.draw_wall()
        ppp.draw_wall()
        aaa.draw_wall()
        sss.draw_wall()
        if sprite.collide_rect(hero, treasure):
            Finish = True
            print("Победил")
        if sprite.collide_rect(hero, cyborg) or sprite.collide_rect(hero, ppp) or sprite.collide_rect(hero, aaa) or sprite.collide_rect(hero, sss):
            Finish = True
            print("Проиграл")
    for e in event.get():
        if e.type == QUIT:
        
            game = False
        
    display.update()