import pygame as pg
import pygame.gfxdraw as gd
from settings import *

vec = pg.math.Vector2

# sprites images
princessImg = pg.image.load(princessImg)
mulanImg = pg.image.load(mulanImg)
elsaImg = pg.image.load(elsaImg)
jasmineImg = pg.image.load(jasmineImg)
enemyImg = pg.image.load(enemyImg)
quickEnemyImg = pg.image.load(quickEnemyImg)
platformImg = pg.image.load(platformImg)
swordImg = pg.image.load(swordImg)
enemySwordImg = pg.image.load(enemySwordImg)
fireImg = pg.image.load(fireImg)
iceImg = pg.image.load(iceImg)
flyEnemyImg = pg.image.load(flyEnemyImg)
fortressImg = pg.image.load(fortressImg)
dragonImg = pg.image.load(dragonImg)

runMulan = [pg.image.load("image/princess/Run (1).png"),pg.image.load("image/princess/Run (2).png"),pg.image.load("image/princess/Run (3).png"),
        pg.image.load("image/princess/Run (4).png"),pg.image.load("image/princess/Run (5).png"), pg.image.load("image/princess/Run (6).png"),
        pg.image.load("image/princess/Run (7).png"), pg.image.load("image/princess/Run (8).png"),pg.image.load("image/princess/Run (9).png"),
        pg.image.load("image/princess/Run (10).png"),pg.image.load("image/princess/Run (11).png"), pg.image.load("image/princess/Run (12).png"),
        pg.image.load("image/princess/Run (13).png"), pg.image.load("image/princess/Run (14).png"), pg.image.load("image/princess/Run (15).png"),
        pg.image.load("image/princess/Run (16).png"), pg.image.load("image/princess/Run (17).png"),pg.image.load("image/princess/Run (17).png"),
        pg.image.load("image/princess/Run (18).png"),pg.image.load("image/princess/Run (19).png"),pg.image.load("image/princess/Run (20).png")]

jumpMulan = [pg.image.load("image/princess/Jump (1).png"),pg.image.load("image/princess/Jump (2).png"),pg.image.load("image/princess/Jump (3).png"),
        pg.image.load("image/princess/Jump (4).png"),pg.image.load("image/princess/Jump (5).png"), pg.image.load("image/princess/Jump (6).png"),
        pg.image.load("image/princess/Jump (7).png"), pg.image.load("image/princess/Jump (8).png"),pg.image.load("image/princess/Jump (9).png"),
        pg.image.load("image/princess/Jump (10).png"),pg.image.load("image/princess/Jump (11).png"), pg.image.load("image/princess/Jump (12).png"),
        pg.image.load("image/princess/Jump (13).png"), pg.image.load("image/princess/Jump (14).png"), pg.image.load("image/princess/Jump (15).png"),
        pg.image.load("image/princess/Jump (16).png"), pg.image.load("image/princess/Jump (17).png"),pg.image.load("image/princess/Jump (17).png"),
        pg.image.load("image/princess/Jump (18).png"),pg.image.load("image/princess/Jump (19).png"),pg.image.load("image/princess/Jump (20).png"),
        pg.image.load("image/princess/Jump (21).png"),pg.image.load("image/princess/Jump (22).png"),pg.image.load("image/princess/Jump (23).png"),
        pg.image.load("image/princess/Jump (24).png"),pg.image.load("image/princess/Jump (25).png"), pg.image.load("image/princess/Jump (26).png"),
        pg.image.load("image/princess/Jump (27).png"), pg.image.load("image/princess/Jump (28).png"),pg.image.load("image/princess/Jump (29).png"),
        pg.image.load("image/princess/Jump (30).png")]

runJasmine = [ pg.image.load("image/mulan/Run1.png"),pg.image.load("image/mulan/Run2.png"), pg.image.load("image/mulan/Run3.png"),
               pg.image.load("image/mulan/Run4.png"), pg.image.load("image/mulan/Run5.png"), pg.image.load("image/mulan/Run6.png"),
               pg.image.load("image/mulan/Run7.png"),pg.image.load("image/mulan/Run8.png"), pg.image.load("image/mulan/Run9.png"),
               pg.image.load("image/mulan/Run10.png")]

jumpJasmine = [pg.image.load("image/mulan/Jump1.png"),pg.image.load("image/mulan/Jump2.png"),
        pg.image.load("image/mulan/Jump3.png"),pg.image.load("image/mulan/Jump4.png"), pg.image.load("image/mulan/Jump5.png"),
        pg.image.load("image/mulan/Jump6.png"), pg.image.load("image/mulan/Jump7.png"),pg.image.load("image/mulan/Jump8.png"),
        pg.image.load("image/mulan/Jump9.png"),pg.image.load("image/mulan/Jump10.png")]


runElsa = [ pg.image.load("image/jasmine/Run (1).png"),pg.image.load("image/jasmine/Run (2).png"),pg.image.load("image/jasmine/Run (3).png"),
        pg.image.load("image/jasmine/Run (4).png"),pg.image.load("image/jasmine/Run (5).png"), pg.image.load("image/jasmine/Run (6).png"),
        pg.image.load("image/jasmine/Run (7).png"), pg.image.load("image/jasmine/Run (8).png")]

jumpElsa = [pg.image.load("image/jasmine/Jump (1).png"),pg.image.load("image/jasmine/Jump (2).png"),pg.image.load("image/jasmine/Jump (3).png"),
        pg.image.load("image/jasmine/Jump (4).png"),pg.image.load("image/jasmine/Jump (5).png"), pg.image.load("image/jasmine/Jump (6).png"),
        pg.image.load("image/jasmine/Jump (7).png"), pg.image.load("image/jasmine/Jump (8).png"),pg.image.load("image/jasmine/Jump (9).png"),
        pg.image.load("image/jasmine/Jump (10).png")]

# create a super class princess that can enable shared characteristics
class Princess(pg.sprite.Sprite):
    score = 0
    reward = 0
    life = 3
    blood = 1000
    hBarL = princesshBarL

    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        Princess.score = 0
        Princess.reward = 0
        Princess.life = 3
        Princess.blood = 1000
        Princess.hBarL = princesshBarL
        self.game = game
        self.w = princessWidth
        self.h = princessHeight
        self.image = princessImg
        self.rect = self.image.get_rect()
        self.rect.midbottom = (initialX, initialY)
        self.pos = vec(initialX, initialY)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.maxSpeed = 50
        self.start = False
        self.attacked = False
        self.ishitFire = False
        self.blood = Princess.blood
        self.hBarL = Princess.hBarL
        self.isfly = False
        self.run = False
        self.isJump = False
        self.runCount = 0
        self.jumpCount = 0
        self.floating = False

    def update(self):
        if self.run == True:
            self.runCount += 1
            if self.runCount > 20:
                self.runCount = 0
        if self.run == False:
            self.runCount = 0
        if self.vel.y != 0 and self.isfly == False:
            self.isJump = True
            self.jumpCount += 1
            if self.jumpCount > 30:
                self.jumpCount = 0
        if self.vel.y == 0:
            self.isJump = False
        if self.isfly == False:
            self.acc = vec(0, playerGravity)
            keys = pg.key.get_pressed()
            if keys[pg.K_LEFT]:
                self.run = True
                self.acc.x = -playerAcc
            elif keys[pg.K_RIGHT]:
                self.run = True
                self.acc.x = playerAcc
            # code from:https://github.com/kidscancode/pygame_tutorials/blob/master/platform/part%202/sprites.py
            self.acc.x += self.vel.x * playerFriction
            self.vel += self.acc
            if self.vel.y >= 10:
                self.vel.y = 10
            if self.vel.x >= self.maxSpeed:
                self.vel.x = self.maxSpeed
            self.pos += self.vel + 0.5 * self.acc
            self.rect.midbottom = self.pos

    def jump(self):
        hits = pg.sprite.spritecollide(self.game.princess, self.game.platforms, False)
        if hits:
            self.vel.y = -23

    def collectReward(self):
        rewardHits = pg.sprite.spritecollide(self, self.game.rewards, True)
        if rewardHits:
            Princess.reward += 1

    def drawRewardN(self):
        font = pg.font.Font("StaySafe-Regular.ttf", 30)
        number = font.render(": " + str(Princess.reward), True, (0, 0, 0))
        self.game.screen.blit(number, (rwNumberX, rwNumberY))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def drawScore(self):
        font = pg.font.Font("StaySafe-Regular.ttf", 30)
        score = font.render("Score: " + str(Princess.score), True, (0, 0, 0))
        self.game.screen.blit(score, (scoreX, scoreY))

    def drawHealthBar(self):
        x = self.pos.x - princessWidth/2
        y  = self.pos.y - princessHeight
        font = pg.font.Font("StaySafe-Regular.ttf", 20)
        health = font.render(str(Princess.blood), True, black)
        self.game.screen.blit(health, (x - 40, y - 40))
        image1 = pg.Surface((princesshBarL, princesshBarH))
        image1.fill(black)
        rect1 = image1.get_rect()
        rect1.x = x - 10
        rect1.y = y - 30
        self.game.screen.blit(image1, rect1)
        if Princess.hBarL > 0:
         pg.draw.rect(self.game.screen, lightred, (rect1.x, rect1.y, Princess.hBarL, princesshBarH))

    def showLostBlood(self):
        x = self.rect.x
        y = self.rect.y - 50
        font = pg.font.Font("StaySafe-Regular.ttf", 20)
        blood1 = font.render("hp -" + str(1), True, red)
        blood2 = font.render("hp -" + str(10), True, red)
        if self.attacked == True:
           self.game.screen.blit(blood1, (x, y))
        if self.ishitFire == True:
           self.game.screen.blit(blood2, (x, y))


    def hitFire(self):
        hits =  pg.sprite.spritecollide(self, self.game.fires, False)
        if hits:
            self.ishitFire = True
            Princess.blood -= 10
            Princess.hBarL -= 10/Princess.blood * princesshBarL
            self.vel.x = -20
        else:
            self.ishitFire = False


# create an inherited class Mulan that has her own actions, such as attacking
class Mulan(Princess):
    def __init__(self, game):
        super().__init__(game)
        self.image = princessImg
        self.attack = False

    def isAttack(self):
        Enemyhits = pg.sprite.spritecollide(self, self.game.enemies, False)
        keys = pg.key.get_pressed()
        if Enemyhits:
            if keys[pg.K_q]:
                self.attack = True
                Enemyhits[0].blood -= attackValue
                Enemyhits[0].hBarL -= enemyhBarW / 5
                Princess.score += 10
                if Enemyhits[0].blood == 0:
                    Enemyhits[0].kill()
                    self.attacked = False


    def draw(self,screen):
        if self.run == True:
          self.image = runMulan[self.runCount]
        elif self.isJump == True:
           self.image = jumpMulan[self.jumpCount]
        else:
          self.image = princessImg
        screen.blit(self.image, self.rect)



# create an inherited class Elsa that has her own actions, such as freezing
class Elsa(Princess):
    def __init__(self, game):
        super().__init__(game)
        # self.image = elsaImg

    def shoot(self):
        self.game.ice.display = True

    def update(self):
        if self.run == True:
            self.runCount += 1
            if self.runCount > 7:
                self.runCount = 0
        if self.run == False:
            self.runCount = 0
        if self.vel.y != 0 and self.isfly == False:
            self.isJump = True
            self.jumpCount += 1
            if self.jumpCount > 9:
                self.jumpCount = 0
        if self.vel.y == 0:
            self.isJump = False
        if self.isfly == False:
            self.acc = vec(0, playerGravity)
            keys = pg.key.get_pressed()
            if keys[pg.K_LEFT]:
                self.run = True
                self.acc.x = -playerAcc
            elif keys[pg.K_RIGHT]:
                self.run = True
                self.acc.x = playerAcc
            # code from:https://github.com/kidscancode/pygame_tutorials/blob/master/platform/part%202/sprites.py
            self.acc.x += self.vel.x * playerFriction
            self.vel += self.acc
            if self.vel.y >= 10:
                self.vel.y = 10
            if self.vel.x >= self.maxSpeed:
                self.vel.x = self.maxSpeed
            self.pos += self.vel + 0.5 * self.acc
            self.rect.midbottom = self.pos

    def draw(self, screen):
        if self.run == True:
            self.image = runElsa[self.runCount]
        elif self.isJump == True:
            self.image = jumpElsa[self.jumpCount]
        else:
            self.image = elsaImg
        screen.blit(self.image, self.rect)


class Ice(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = iceImg
        self.rect = self.image.get_rect()
        self.rect.center = (0,0)
        self.display = False
        self.vx = 15
        self.distance = 0

    def update(self):
         self.distance = abs(self.rect.x - self.game.elsa.rect.x)
         if self.distance > 200:
             self.display = False
         if self.display == False:
            self.rect.x = self.game.elsa.rect.x + princessWidth
            self.rect.y = self.game.elsa.rect.y + princessHeight/3
         else:
            self.rect.x += self.vx
            self.rect.y = self.game.elsa.rect.y + princessHeight / 3
            hitsFire = pg.sprite.spritecollide(self, self.game.fires, False)
            hitsEnemy = pg.sprite.spritecollide(self, self.game.enemies, False)
            if hitsFire:
                self.display = False
                for fire in hitsFire:
                    fire.strength -= 10
                    if fire.strength == 0:
                        fire.kill()
            if hitsEnemy:
                self.display = False
                hitsEnemy[0].vx = 0
                hitsEnemy[0].freeze = True

    def draw(self):
        if self.display == True:
         self.game.screen.blit(self.image, self.rect)



# create an inherited class Jasmine that has her own actions, such as flying
class Jasmine(Princess):
    def __init__(self, game):
        super().__init__(game)

    def update(self):
        if self.run == True:
            self.runCount += 1
            if self.runCount > 9:
                self.runCount = 0
        if self.run == False:
            self.runCount = 0
        if self.isfly == False and self.vel.y != 0:
            self.isJump = True
            self.jumpCount += 1
            if self.jumpCount > 9:
                self.jumpCount = 0
        if self.vel.y == 0:
            self.isJump = False
        self.acc = vec(0, playerGravity)
        keys = pg.key.get_pressed()
        if self.floating == True:
            self.vel.y = 0
            self.acc.y = 0
            if keys[pg.K_LEFT]:
                self.run = False
                self.acc.x = -playerAcc
            elif keys[pg.K_RIGHT]:
                self.run = False
                self.acc.x = playerAcc
            elif keys[pg.K_f]:
                self.isJump = False
                self.isfly = True
                self.acc.y = -1.8
                self.vel.y += self.acc.y
        else:
            self.isfly = False
            self.floating = False
            if keys[pg.K_LEFT]:
                self.run = True
                self.acc.x = -playerAcc
            elif keys[pg.K_RIGHT]:
                self.run = True
                self.acc.x = playerAcc
            elif keys[pg.K_f]:
                self.isJump = False
                self.isfly = True
                self.acc.y = -1.8
        # code from:https://github.com/kidscancode/pygame_tutorials/blob/master/platform/part%202/sprites.py
        self.acc.x += self.vel.x * playerFriction
        self.vel += self.acc
        if self.vel.y >= 10:
            self.vel.y = 10
        if self.vel.y <= -20:
            self.vel.y = -20
        if self.vel.x >= self.maxSpeed:
            self.vel.x = self.maxSpeed
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos
        if self.pos.y <= 100:
            self.pos.y = 100

    def draw(self, screen):
        if self.run == True:
            self.image = runJasmine[self.runCount]
        elif self.isJump == True:
            self.image = jumpJasmine[self.jumpCount]
        else:
            self.image = jasmineImg
        screen.blit(self.image, self.rect)


class Carpet(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((carpetW,carpetH))
        self.image.fill(purple)
        self.rect = self.image.get_rect()
        self.rect.center = (0,0)
        self.display = False


    def update(self):
        self.rect.x = self.game.jasmine.rect.x - 30
        self.rect.y = self.game.jasmine.pos.y
        if self.game.jasmine.isfly == True or self.game.jasmine.floating == True:
            self.display = True
        else:
            self.display = False

    def draw(self):
        if self.display == True:
            self.game.screen.blit(self.image,self.rect)




# create a super class for all the enemies
class Enemy(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = enemyImg
        self.game = game
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vx = -15
        self.blood = 100
        self.alive = True
        self.isAttack = False
        self.freeze = False
        self.distance = 0
        self.move = True
        self.timeElapsed = 0
        self.hBarL = enemyhBarW

    def drawSword(self):
        image = enemySwordImg
        rect = image.get_rect()
        x1 = self.rect.x
        y1 = self.rect.y + enemySize / 2
        rect.center = (x1, y1)
        if self.isAttack == True and self.freeze == False:
            self.game.screen.blit(image, rect)

    def update(self):
        self.distance = ((self.rect.x - self.game.princess.rect.x)**2 + (self.rect.y - self.game.princess.rect.y)**2)**0.5
        if self.move == True:
            self.rect.x += self.vx
            if self.rect.x < 0:
                self.vx = -self.vx
            if self.rect.x + enemySize > width:
                self.vx = -self.vx

    def showLostBlood(self):
        x = self.rect.x
        y = self.rect.y - 80
        font = pg.font.Font("StaySafe-Regular.ttf", 20)
        blood = font.render("hp -" + str(attackValue), True, blue)
        self.game.screen.blit(blood, (x, y))

    def attack(self):
        if self.isAttack == True and not self.freeze:
            Princess.blood -= 1
            Princess.hBarL -=  1/princessBlood * princesshBarL
            self.game.princess.vel.x = -5
            self.game.princess.attacked = True

    def drawHealthBar(self):
        image1 = pg.Surface((enemyhBarW, enemyhBarH))
        image1.fill(black)
        rect1 = image1.get_rect()
        rect1.x = self.rect.x
        rect1.y = self.rect.y - enemySize / 2 - 5
        self.game.screen.blit(image1, rect1)
        if self.hBarL > 0:
         pg.draw.rect(self.game.screen, blue, (rect1.x, rect1.y, self.hBarL, enemyhBarH))



# create an inherited class for enemies that are moving very fast
class QuickEnemy(Enemy):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = quickEnemyImg
        self.vx = 20


# create an inherited class for enemies that can shoot the player
class FlyingEnemy(Enemy):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = flyEnemyImg
        self.vx = 10



# create an inherited class for the boss
class Dragon(Enemy):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = dragonImg
        self.vx = 0


# create a class for the platform to Jump on

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(platformColor)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = w
        self.height = h


    def getHashables(self):
        return (self.rect.x, self.rect.y, self.width, self.height)  # return a tuple of hashables

    def __hash__(self):
        return hash(self.getHashables())

    def __eq__(self, other):
        return (isinstance(other, Platform) and self.rect.x == other.rect.x and self.rect.y == other.rect.y and
                self.width == other.width and self.height == other.height)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Reward(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h, r):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(white)
        self.image.set_colorkey(white)
        self.game = game
        self.screen = self.game.screen
        # where the circle is drawn
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.r = r
        self.color = rewardColor

    def drawCircle(self):
        pg.draw.circle(self.screen, self.color, self.rect.center, self.r)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Sword(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = swordImg
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)
        self.display = False

    def update(self):
        x = self.game.mulan.pos.x + (self.game.mulan.w) / 1.5
        y = self.game.mulan.pos.y - self.game.mulan.h / 1.5
        self.rect.center = (x, y)

    def draw(self):
        if self.display == True:
            self.game.screen.blit(self.image, self.rect)


class Fire(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = fireImg
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)
        self.strength = 50

    def update(self):
        self.rect.x -= self.game.princess.vel.x

    def draw(self):
        self.game.screen.blit(self.image, self.rect)



class Castle(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = fortressImg
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self):
        self.game.screen.blit(self.image, self.rect)

    def update(self):
        self.rect.x -= self.game.princess.vel.x



