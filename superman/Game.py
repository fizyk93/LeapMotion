#############################################
#   Author: Sam Grogan A.K.A (Gh0st)        #
#   Release Date:                           #
#   License: GNU GPL                        #
#   Project Name: Superman                  #
#   Version: 2.0                            #
#############################################
import pygame, random, sys

pygame.init()

screen = pygame.display.set_mode((900, 700),pygame.FULLSCREEN)
class Superman(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("superman.gif")
        print "SUPERMAN!"
        self.rect = self.image.get_rect()
        self.rect.inflate_ip(-10,-10)
               
        if not pygame.mixer:
            print "NO sound!!!"
        else:
            pygame.mixer.init()
            
            self.explosion = pygame.mixer.Sound("explosion.ogg")
            self.collect = pygame.mixer.Sound("pickup.wav")
        
    def update(self):
        mousex, mousey = pygame.mouse.get_pos()
        self.rect.centerx = mousex
        self.rect.centery = mousey
        
    
        
class KryptoX(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("kryptox.gif")
        self.rect = self.image.get_rect()
        self.reset()

        self.dy = 7

    def update(self):
        self.rect.centery += self.dy
        if self.rect.top > screen.get_height():
            self.reset()

    def reset(self):
        self.rect.top = 0
        self.rect.centerx = random.randrange(0, screen.get_width())

class Kryptonite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("kryptonite.gif")
        self.rect = self.image.get_rect()
        self.rect.inflate_ip(-40, -40)
        self.reset()
    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        if self.rect.top > screen.get_width():
            self.reset()

    def reset(self):
        self.rect.bottom = 0
        self.rect.centerx = random.randrange(0, screen.get_height())
        self.dx = random.randrange(-4,4)
        self.dy = random.randrange(5,10)
        
class Space(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("space.jpg")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.dy = 40
        self.reset()
    def update(self):
        self.rect.bottom += self.dy
        if self.rect.top >= 0:
            self.reset()
    def reset(self):
        self.rect.bottom = screen.get_height()

class Score(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.lives = 6
        self.score = 0
        self.font = pygame.font.Font("Smallville1.ttf",40)

    def update(self):
        self.text = "Lives: %d Score: %d"%(self.lives,self.score)
        self.image = self.font.render(self.text,1,(235,245,225))
        self.rect = self.image.get_rect()
    def Up_score(self):
        self.score += 50
    
class PowerUp(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("powerup.gif")
        self.rect = self.image.get_rect()
        self.dy = 3
    
        self.rect.inflate_ip(-10,-10)
    def update(self):
        self.rect.centery += self.dy
        if self.rect.top > screen.get_height():
            self.reset()
        

    def reset(self):
        self.rect.top = 0
        self.rect.centerx = random.randrange(0, screen.get_width())

class HeatVision(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("heatvision.png")
        self.rect = self.image.get_rect()
        self.dy = 17
        self.rect.center = pygame.mouse.get_pos()
        
    def update(self):
        self.rect.centery -= self.dy
        
class Darkseid(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("darkside.gif")
        self.rect = self.image.get_rect()
        self.dy = 6
        self.rect.inflate_ip(-10,-20)
       
    def update(self):
        self.rect.centery += self.dy
        if self.rect.top > screen.get_height():
            self.reset()
    def reset(self):
        self.rect.top = 0
        self.rect.centerx = random.randrange(0, screen.get_width())

hv = HeatVision()

weaponSprites = pygame.sprite.Group()            
def chkey():
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        weaponSprites.add(hv)
        hv.rect.center = pygame.mouse.get_pos()
    
       
def game():
    pygame.display.set_caption("Superman")
    kryptox = KryptoX()
    dark = Darkseid()   
    k1 = Kryptonite()
    k2 = Kryptonite()
    k3 = Kryptonite()
    k4 = Kryptonite()
    k5 = Kryptonite()
    space = Space()
    score = Score()
    powerup = PowerUp()
    superman = Superman()
    goodSprites = pygame.sprite.Group(space,kryptox,superman)
    badSprites = pygame.sprite.Group(k1,k2,k3,k4,k5,dark)
    scoreSprite = pygame.sprite.Group(score)
    powerUpSprites = pygame.sprite.Group(powerup)
    pygame.mixer.music.load("theme.mp3")
    pygame.mixer.music.play(-1)
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(40)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    keepGoing = False
                if pygame.key.get_pressed()[pygame.K_t]:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("Remy Zero_ Save Me (Theme from Smallville).mp3")
                    pygame.mixer.music.play(-1)
                if pygame.key.get_pressed()[pygame.K_a]:
                    hv.image = pygame.image.load("freezebreath.png")
                if pygame.key.get_pressed()[pygame.K_s]:
                    hv.image = pygame.image.load("heatvision.png")
                chkey()
                
                if hv.rect.top <= 0:
                    weaponSprites.remove(hv)
                    chkey()
        
        
        if superman.rect.colliderect(kryptox.rect):
            kryptox.reset()
            score.Up_score()
            superman.collect.play()
        

        hitK = pygame.sprite.spritecollide(superman,badSprites,False)
        if hitK:
            score.lives -= 1
            if score.lives <= 0:
                keepGoing = False
              
                
	for theK in hitK:
            theK.reset()

        
        goodSprites.update()
        goodSprites.draw(screen)
        badSprites.update()
        badSprites.draw(screen)
        scoreSprite.update()
        scoreSprite.draw(screen)
        weaponSprites.draw(screen)
        weaponSprites.update()
        
        if superman.rect.colliderect(powerup.rect):
            score.lives += 1
            score.score -= 200
            powerup.reset()
        if score.score >= 1000:
            kryptox.dy = 12
            powerUpSprites.update()
            powerUpSprites.draw(screen)
            
        if score.score >= 2000:
            powerUpSprites.remove(powerup)

        if score.score >= 5000:
            kryptox.dy = 13
            powerUpSprites.draw(screen)
            powerUpSprites.update()
        
            
        if score.score >= 6000:
            powerUpSprites.remove(powerup)
        
        if hv.rect.colliderect(dark.rect):
            weaponSprites.remove(hv)
            score.score += 100
            superman.explosion.play()
            dark.reset()

        if score.score >= 10000:
            kryptox.dy = 14
        
        
        pygame.display.flip()
    
    #return mouse cursor
    pygame.mouse.set_visible(True)
    pygame.mixer.music.stop()
    return score.score


def intro(score):
    space = Space()
    superman = Superman()
    pygame.display.set_caption("Superman")
    goodSprites = pygame.sprite.Group(space, superman)

    insFont = pygame.font.Font("Smallville1.ttf",45)

    instructions = (
    "Superman!     Last score: %d" % score ,
    "",
    "Instructions:  You are Superman,",
    "",
    "Flying through space",
    "",
    "Earth is under attack by kryptonite that can",
    "harm humans and superman.",
    "",
    "But there is a cure Kryto-X which" ,
    "",
    "Superman must collect to save ",
    "earth",
    "",
    "good luck!",
    "",
    "click to start, escape to quit..."
    )

    insLabels = []
    for line in instructions:
        tempLabel = insFont.render(line,1,(255,255,255))
        insLabels.append(tempLabel)
    pygame.mixer.music.load('KryptonDestroyed.mp3')
    pygame.mixer.music.play(-1)
    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                donePlaying = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                keepGoing = False
                donePlaying = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keepGoing = False
                    donePlaying = True
        goodSprites.update()
        goodSprites.draw(screen)

        for i in range(len(insLabels)):
            screen.blit(insLabels[i], (50,30*i))

        pygame.display.flip()
    pygame.mixer.music.stop()
    return donePlaying
    
def main():
    donePlaying = False
    score = 0
    while not donePlaying:
        donePlaying = intro(score)
        if not donePlaying:
            score = game()


        
    
if __name__ == "__main__":
    main()
