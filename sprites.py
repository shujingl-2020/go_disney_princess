import pygame as pg
import pygame.gfxdraw as gd
from settings import *

vec = pg.math.Vector2


# breadth first search algorithm
# tutorial: https://www.youtube.com/watch?v=oDqjPvD54Ss
# get the starting point
def getSource(matrix):
    result = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "S":
                result = (i, j)
    return result


# get the target point
def getDestination(matrix):
    result = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "E":
                result = (i, j)
    return result


# get all the points that are adjancent to it
def getNeighbors(currentCell, matrix, visited):
    direction = [(-1, -1), (0, -1), (1, -1),
                 (-1, 0), (0, 0), (1, 0),
                 (-1, 1), (0, -1), (1, 1)]
    result = []
    (r, c) = currentCell
    for dir in direction:
        if dir != (0, 0):
            (dr, dc) = dir
            newr = r + dr
            newc = c + dc
            if (newr >= 0 and newr < len(matrix) and newc >= 0 and newc < len(matrix[0])
                    and (matrix[newr][newc] == 1 or matrix[newr][newc] == "E") and visited[newr][newc] == False):
                result.append((newr, newc))
    return result


# avoid a cell being visited twice
def getVisited(r, c):
    visited = []
    for i in range(r):
        row = []
        for j in range(c):
            row.append(False)
        visited.append(row)
    return visited


# keep track of the parent node
def getPrev(r, c):
    prev = []
    for i in range(r):
        row = []
        for j in range(c):
            row.append(None)
        prev.append(row)
    return prev


def updateMatrixE(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "E":
                matrix[i][j] = 1
    return matrix


def updateMatrixS(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "S":
                matrix[i][j] = 1
    return matrix


# get the shortest path
def constructPath(prev, matrix, s):
    target = getDestination(matrix)
    result = [target]
    (tr, tc) = target
    while target != s:
        target = prev[tr][tc]
        (tr, tc) = target
        result.append(target)
    result.pop()
    result = list(reversed(result))
    return result


# using queue
def solve(matrix):
    r = len(matrix)
    c = len(matrix[0])
    s = getSource(matrix)
    q = [s]
    (row, col) = s
    visited = getVisited(r, c)
    visited[row][col] = True
    prev = getPrev(r, c)
    while len(q) > 0:
        node = q.pop(0)
        neighbors = getNeighbors(node, matrix, visited)
        for cell in neighbors:
            (row1, col1) = cell
            if visited[row1][col1] == False:
                q.append(cell)
                visited[row1][col1] = True
                prev[row1][col1] = node
    result = constructPath(prev, matrix, s)
    return result


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
finalfightImg = pg.image.load(finalfightImg)
attackfireImg = pg.image.load(attackfireImg)
axeEnemyImg = pg.image.load(axeEnemyImg)
lifeImg = pg.image.load(lifeImg)
freezeImg = pg.image.load(freezeImg)
freezefireImg = pg.image.load(freezefireImg)
axeImg = pg.image.load(axeImg)
ballImg = pg.image.load(ballImg)
bigballImg = pg.image.load(bigballImg)
potionImg = pg.image.load(medicineImg)
celebrationImg = pg.image.load(celebrationImg)

runMulan = [pg.image.load("image/princess/Run (1).png"), pg.image.load("image/princess/Run (2).png"),
            pg.image.load("image/princess/Run (3).png"),
            pg.image.load("image/princess/Run (4).png"), pg.image.load("image/princess/Run (5).png"),
            pg.image.load("image/princess/Run (6).png"),
            pg.image.load("image/princess/Run (7).png"), pg.image.load("image/princess/Run (8).png"),
            pg.image.load("image/princess/Run (9).png"),
            pg.image.load("image/princess/Run (10).png"), pg.image.load("image/princess/Run (11).png"),
            pg.image.load("image/princess/Run (12).png"),
            pg.image.load("image/princess/Run (13).png"), pg.image.load("image/princess/Run (14).png"),
            pg.image.load("image/princess/Run (15).png"),
            pg.image.load("image/princess/Run (16).png"), pg.image.load("image/princess/Run (17).png"),
            pg.image.load("image/princess/Run (17).png"),
            pg.image.load("image/princess/Run (18).png"), pg.image.load("image/princess/Run (19).png"),
            pg.image.load("image/princess/Run (20).png")]

jumpMulan = [pg.image.load("image/princess/Jump (1).png"), pg.image.load("image/princess/Jump (2).png"),
             pg.image.load("image/princess/Jump (3).png"),
             pg.image.load("image/princess/Jump (4).png"), pg.image.load("image/princess/Jump (5).png"),
             pg.image.load("image/princess/Jump (6).png"),
             pg.image.load("image/princess/Jump (7).png"), pg.image.load("image/princess/Jump (8).png"),
             pg.image.load("image/princess/Jump (9).png"),
             pg.image.load("image/princess/Jump (10).png"), pg.image.load("image/princess/Jump (11).png"),
             pg.image.load("image/princess/Jump (12).png"),
             pg.image.load("image/princess/Jump (13).png"), pg.image.load("image/princess/Jump (14).png"),
             pg.image.load("image/princess/Jump (15).png"),
             pg.image.load("image/princess/Jump (16).png"), pg.image.load("image/princess/Jump (17).png"),
             pg.image.load("image/princess/Jump (17).png"),
             pg.image.load("image/princess/Jump (18).png"), pg.image.load("image/princess/Jump (19).png"),
             pg.image.load("image/princess/Jump (20).png"),
             pg.image.load("image/princess/Jump (21).png"), pg.image.load("image/princess/Jump (22).png"),
             pg.image.load("image/princess/Jump (23).png"),
             pg.image.load("image/princess/Jump (24).png"), pg.image.load("image/princess/Jump (25).png"),
             pg.image.load("image/princess/Jump (26).png"),
             pg.image.load("image/princess/Jump (27).png"), pg.image.load("image/princess/Jump (28).png"),
             pg.image.load("image/princess/Jump (29).png"),
             pg.image.load("image/princess/Jump (30).png")]

runJasmine = [pg.image.load("image/mulan/Run1.png"), pg.image.load("image/mulan/Run2.png"),
              pg.image.load("image/mulan/Run3.png"),
              pg.image.load("image/mulan/Run4.png"), pg.image.load("image/mulan/Run5.png"),
              pg.image.load("image/mulan/Run6.png"),
              pg.image.load("image/mulan/Run7.png"), pg.image.load("image/mulan/Run8.png"),
              pg.image.load("image/mulan/Run9.png"),
              pg.image.load("image/mulan/Run10.png")]

jumpJasmine = [pg.image.load("image/mulan/Jump1.png"), pg.image.load("image/mulan/Jump2.png"),
               pg.image.load("image/mulan/Jump3.png"), pg.image.load("image/mulan/Jump4.png"),
               pg.image.load("image/mulan/Jump5.png"),
               pg.image.load("image/mulan/Jump6.png"), pg.image.load("image/mulan/Jump7.png"),
               pg.image.load("image/mulan/Jump8.png"),
               pg.image.load("image/mulan/Jump9.png"), pg.image.load("image/mulan/Jump10.png")]

runElsa = [pg.image.load("image/jasmine/Run (1).png"), pg.image.load("image/jasmine/Run (2).png"),
           pg.image.load("image/jasmine/Run (3).png"),
           pg.image.load("image/jasmine/Run (4).png"), pg.image.load("image/jasmine/Run (5).png"),
           pg.image.load("image/jasmine/Run (6).png"),
           pg.image.load("image/jasmine/Run (7).png"), pg.image.load("image/jasmine/Run (8).png")]

jumpElsa = [pg.image.load("image/jasmine/Jump (1).png"), pg.image.load("image/jasmine/Jump (2).png"),
            pg.image.load("image/jasmine/Jump (3).png"),
            pg.image.load("image/jasmine/Jump (4).png"), pg.image.load("image/jasmine/Jump (5).png"),
            pg.image.load("image/jasmine/Jump (6).png"),
            pg.image.load("image/jasmine/Jump (7).png"), pg.image.load("image/jasmine/Jump (8).png"),
            pg.image.load("image/jasmine/Jump (9).png"),
            pg.image.load("image/jasmine/Jump (10).png")]


# create a super class princess that can enable shared characteristics
class Princess(pg.sprite.Sprite):
    score = 0
    reward = 0
    life = 3
    blood = 500
    hBarL = princesshBarL
    alive = True
    finalMatrix = matrix

    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.initializeClassAttribute()
        self.initializePos()
        self.game = game
        self.attacked = False
        self.ishitFire = False
        self.isfly = False
        self.run = False
        self.isJump = False
        self.runCount = 0
        self.jumpCount = 0
        self.floating = False
        self.hitbyfireball = False
        self.hitbyAxe = False
        self.timeElapsed = 0
        self.mousePosition = (0,0)

    def initializePos(self):
        self.w = princessWidth
        self.h = princessHeight
        self.image = princessImg
        self.rect = self.image.get_rect()
        self.rect.midbottom = (initialX, initialY)
        self.pos = vec(initialX, initialY)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.maxSpeed = 100

    def initializeClassAttribute(self):
        Princess.score = 0
        Princess.reward = 0
        Princess.life = 3
        Princess.blood = 500
        Princess.hBarL = princesshBarL
        Princess.alive = True


    def updateMatrix(self):
        Princess.finalMatrix = self.game.matrix
        (x, y) = self.rect.center
        if x > self.game.finalplatX:
            xdistance = x - self.game.finalplatX
            vecR = int((y - 50) // cellH)
            vecC = int((xdistance) // cellW)
            if vecR >= 0 and vecR < rows and vecC >= 0 and vecC < cols and Princess.finalMatrix[vecR][vecC] != 0 and \
                    Princess.finalMatrix[vecR][vecC] != "S":
                Princess.finalMatrix = updateMatrixE(Princess.finalMatrix)
                Princess.finalMatrix[vecR][vecC] = "E"

    def updateImg(self):
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


    def updateMovement(self):
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
            if self.vel.x > self.maxSpeed:
                self.vel.x = self.maxSpeed
            self.pos += self.vel + 0.5 * self.acc
            self.rect.midbottom = self.pos
            if self.rect.x < 20:
                self.rect.x = 20
            if self.rect.x + 60 > width:
                self.rect.x = width - 60
            if self.rect.y < 50:
                self.rect.y = 50
            if self.pos.y > initialBottom + 20:
                self.rect.x = self.game.finalplatX
                self.rect.y = cellH + (cellH - finalPlatH) + 50 - 60
                Princess.alive = False
            if Princess.blood <= 0:
                Princess.life -= 1
                if Princess.life > 0:
                    Princess.blood = 500
                    Princess.hBarL = princesshBarL
                else:
                    Princess.alive = False
                    self.game.princess.kill()


    def update(self):
        self.updateMatrix()
        self.updateImg()
        self.updateMovement()
        self.hitbyFireball()
        self.hitFire()
        self.collectReward()

    def hitFire(self):
        hits = pg.sprite.spritecollide(self, self.game.fires, False)
        if hits:
            self.ishitFire = True
            Princess.blood -= 10
            Princess.hBarL -= 10 / princessBlood * princesshBarL
            self.vel.x = -20
        else:
            self.ishitFire = False


    def hitbyFireball(self):
        hits = pg.sprite.spritecollide(self, self.game.fireballs, False)
        if hits:
            self.hitbyfireball = True
            Princess.blood -= 5
            Princess.hBarL -= 5 / princessBlood * princesshBarL
            # if hits[0].rect.x < self.rect.x:
            #     self.vel.x = 5
            # if hits[0].rect.x > self.rect.x:
            #     self.vel.x = -5
            hits[0].display = False
        else:
            self.hitbyfireball = False

    def collectReward(self):
        rewardHits = pg.sprite.spritecollide(self, self.game.rewards, True)
        if rewardHits:
            Princess.reward += 1

    def jump(self):
        hits1 = pg.sprite.spritecollide(self.game.princess, self.game.platforms, False)
        hits2 = pg.sprite.spritecollide(self.game.princess, self.game.finalplatforms, False)
        if hits1 or hits2:
            self.vel.y = -23

    def draw(self):
        self.game.screen.blit(self.image, self.rect)
        self.showLostBlood()
        self.drawHealthBar()
        self.drawRewardN()
        self.drawScore()

    def drawRewardN(self):
        font = pg.font.Font("StaySafe-Regular.ttf", 30)
        number = font.render(": " + str(Princess.reward), True, (0, 0, 0))
        self.game.screen.blit(number, (rwNumberX, rwNumberY))

    def drawScore(self):
        font = pg.font.Font("StaySafe-Regular.ttf", 30)
        score = font.render("Score: " + str(Princess.score), True, (0, 0, 0))
        self.game.screen.blit(score, (scoreX, scoreY))

    def drawHealthBar(self):
        x = self.rect.x - 10
        y = self.rect.y
        font = pg.font.Font("StaySafe-Regular.ttf", 20)
        health = font.render(str(Princess.blood), True, black)
        image1 = pg.Surface((princesshBarL, princesshBarH))
        image1.fill(black)
        rect1 = image1.get_rect()
        rect1.x = x - 10
        rect1.y = y - 30
        if Princess.hBarL > 0:
            self.game.screen.blit(health, (x - 40, y - 40))
            self.game.screen.blit(image1, rect1)
            pg.draw.rect(self.game.screen, lightred, (rect1.x, rect1.y, Princess.hBarL, princesshBarH))

    def showLostBlood(self):
        x = self.rect.x
        y = self.rect.y - 50
        font = pg.font.Font("StaySafe-Regular.ttf", 20)
        blood1 = font.render("hp -" + str(1), True, red)
        blood2 = font.render("hp -" + str(10), True, red)
        blood3 = font.render("hp -" + str(5), True, red)
        blood4 = font.render("hp -" + str(5), True, red)
        if self.attacked == True:
            self.game.screen.blit(blood1, (x, y))
        if self.ishitFire == True:
            self.game.screen.blit(blood2, (x, y))
        if self.hitbyfireball == True:
            self.game.screen.blit(blood3, (x, y))
        if self.hitbyAxe == True:
            self.game.screen.blit(blood4, (x, y))


# create an inherited class Mulan that has her own actions, such as attacking
class Mulan(Princess):
    def __init__(self, game):
        super().__init__(game)
        self.attack = False

    def isAttack(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_q]:
                self.game.sword.display = True
                for enemy in self.game.enemies:
                    if enemy.distanceX < 40 and enemy.distanceY < 10:
                        self.attack = True
                        enemy.attacked = True
                        enemy.blood -= attackValue
                        enemy.hBarL -= enemyhBarW / 5
                        if enemy.blood == 0:
                            enemy.kill()
                            Princess.score += 10
                            self.attacked = False

    def update(self):
        self.updateMatrix()
        self.updateImg()
        self.updateMovement()
        self.hitbyFireball()
        self.hitFire()
        self.collectReward()
        self.isAttack()

    def draw(self):
        if self.run == True:
            self.image = runMulan[self.runCount]
        elif self.isJump == True:
            self.image = jumpMulan[self.jumpCount]
        else:
            self.image = princessImg
        self.game.screen.blit(self.image, self.rect)
        self.showLostBlood()
        self.drawHealthBar()
        self.drawRewardN()
        self.drawScore()


# create an inherited class Elsa that has her own actions, such as freezing
class Elsa(Princess):
    def __init__(self, game):
        super().__init__(game)

    def shoot(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
         if self.game.ice.display == False:
            self.game.ice.display = True

    def updateImg(self):
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

    def update(self):
        self.updateMatrix()
        self.updateImg()
        self.updateMovement()
        self.hitbyFireball()
        self.hitFire()
        self.collectReward()
        self.shoot()

    def draw(self):
        if self.run == True:
            self.image = runElsa[self.runCount]
        elif self.isJump == True:
            self.image = jumpElsa[self.jumpCount]
        else:
            self.image = elsaImg
        self.game.screen.blit(self.image, self.rect)
        self.showLostBlood()
        self.drawHealthBar()
        self.drawRewardN()
        self.drawScore()


class Ice(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = iceImg
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)
        self.display = False
        self.vx = 15
        self.distance = 0

    def update(self):
        self.distance = abs(self.rect.x - self.game.elsa.rect.x)
        if self.distance > 200:
            self.display = False
        if self.display == False:
            self.rect.x = self.game.elsa.rect.x + princessWidth
            self.rect.y = self.game.elsa.rect.y + princessHeight / 3
        else:
            self.rect.x += self.vx
            self.rect.y = self.game.elsa.rect.y + princessHeight / 3
            hitsFire = pg.sprite.spritecollide(self, self.game.fires, False)
            hitsEnemy = pg.sprite.spritecollide(self, self.game.enemies, False)
            if hitsFire:
                hitsFire[0].freeze = True
                self.display = False
                for fire in hitsFire:
                    fire.strength -= 10
                    if fire.strength == 0:
                        fire.kill()
            if hitsEnemy:
                self.display = False
                hitsEnemy[0].move = False
                hitsEnemy[0].freeze = True

    def draw(self):
        if self.display == True:
            self.game.screen.blit(self.image, self.rect)


# create an inherited class Jasmine that has her own actions, such as flying
class Jasmine(Princess):
    def __init__(self, game):
        super().__init__(game)
        self.timeElapsed = 0

    def updateMovement(self):
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
        self.updatePost()

    def updatePost(self):
        self.acc.x += self.vel.x * playerFriction
        self.vel += self.acc
        if self.vel.y >= 10:
            self.vel.y = 10
        if self.vel.x >= self.maxSpeed:
            self.vel.x = self.maxSpeed
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos
        if self.rect.x < 20:
            self.rect.x = 20
            self.vel.x = 0
        if self.rect.x + 60 > width:
            self.rect.x = width - 60
            self.vel.x = 0
        if self.rect.y < 50:
            self.rect.y = 50
        if self.pos.y > initialBottom + 20:
            self.rect.x = self.game.finalplatX
            self.rect.y = cellH + (cellH - finalPlatH) + 50 - 60
            Princess.alive = False
        if Princess.blood <= 0:
            Princess.life -= 1
            if Princess.life > 0:
                Princess.blood = 500
                Princess.hBarL = princesshBarL
            else:
                Princess.alive = False
                self.game.princess.kill()


    def flyLimit(self):
        if self.floating == True:
            self.dt = self.game.clock.tick(fps)
            self.timeElapsed += self.dt
            if self.timeElapsed > 300:
                self.isfly = False
                self.floating = False
                self.timeElapsed = 0

    def updateImg(self):
        if self.run == True:
            self.runCount += 1
            if self.runCount > 9:
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

    def update(self):
        self.updateImg()
        self.updateMatrix()
        self.updateMovement()
        #self.flyLimit()
        self.hitbyFireball()
        self.hitFire()
        self.collectReward()

    def draw(self):
        if self.run == True:
            self.image = runJasmine[self.runCount]
        elif self.isJump == True:
            self.image = jumpJasmine[self.jumpCount]
        else:
            self.image = jasmineImg
        self.game.screen.blit(self.image, self.rect)
        self.showLostBlood()
        self.drawHealthBar()
        self.drawRewardN()
        self.drawScore()


class Carpet(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((carpetW, carpetH))
        self.image.fill(purple)
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)
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
            self.game.screen.blit(self.image, self.rect)


# create a super class for all the enemies
class Enemy(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = enemyImg
        self.game = game
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vx = 0
        self.blood = 100
        self.alive = True
        self.isAttack = False
        self.freeze = False
        self.distanceX = 0
        self.distanceY = 0
        self.move = True
        self.timeElapsed = 0
        self.hBarL = enemyhBarW
        self.attacked = False

    def update(self):
        self.distanceX = abs(self.rect.x - self.game.princess.rect.x)
        self.distanceY = abs(self.rect.y - self.game.princess.rect.y)
        if self.distanceX > 40 or self.distanceY > 0:
            if not self.freeze:
                self.move = True
                self.isAttack = False
                self.game.princess.attacked = False
        if self.distanceX > 40:
            if self.game.princess.rect.x < self.rect.x:
                self.vx = -10
            if self.game.princess.rect.x > self.rect.x:
                self.vx = 10
        if self.distanceX <= 40:
            self.move = False
        if self.move == False:
            self.vx = 0
        if self.freeze == True:
            self.move = False
        self.rect.x += self.vx
        self.unFreeze()

    def unFreeze(self):
        if self.freeze == True:
            dt = self.game.clock.tick(fps)
            self.timeElapsed += dt
            if self.timeElapsed >= 400:
                self.freeze = False
                self.timeElapsed = 0

    def attack(self):
        if self.isAttack == True and not self.freeze:
            Princess.blood -= 1
            Princess.hBarL -= 1 / princessBlood * princesshBarL
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

    def drawSword(self):
        image = enemySwordImg
        rect = image.get_rect()
        x1 = self.rect.x
        y1 = self.rect.y + enemySize / 2
        rect.center = (x1, y1)
        if self.isAttack == True and self.freeze == False:
            self.game.screen.blit(image, rect)

    def showLostBlood(self):
        x = self.rect.x
        y = self.rect.y - 80
        font = pg.font.Font("StaySafe-Regular.ttf", 20)
        blood = font.render("hp -" + str(attackValue), True, blue)
        self.game.screen.blit(blood, (x, y))


# create an inherited class for enemies that are moving very fast
class QuickEnemy(Enemy):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = quickEnemyImg
        self.vx = 0

    def update(self):
        self.distanceX = abs(self.rect.x - self.game.princess.rect.x)
        self.distanceY = abs(self.rect.y - self.game.princess.rect.y)
        if self.distanceX > 40 or self.distanceY > 10:
           if not self.freeze:
            self.move = True
            self.isAttack = False
            self.game.princess.attacked = False
        if self.distanceX > 40:
            if self.game.princess.rect.x < self.rect.x:
                self.vx = -15
            if self.game.princess.rect.x > self.rect.x:
                self.vx = 15
        if self.distanceX <= 40:
            self.move = False
        if self.move == False:
            self.vx = 0
        if self.freeze == True:
            self.move = False
        self.rect.x += self.vx
        self.unFreeze()

# create an inherited class for enemies that can shoot the player
class FlyingEnemy(Enemy):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = flyEnemyImg
        self.vx = 0
        self.blood = 50
        self.hitbyball = False
        self.alive = True

    def hitByBall(self):
        if self.hitbyball:
            self.blood -= 10
            self.hBarL -= 10/50 * enemyhBarW

    def update(self):
        if self.blood <= 0:
            self.alive = False
            self.kill()
        self.distance = ((self.rect.x - self.game.princess.rect.x) ** 2 +
                         (self.rect.y - self.game.princess.rect.y) ** 2) ** 0.5
        if self.game.x <= -(plat5X2 - width):
            if self.rect.x <= 0:
                self.vx = 10
            if self.rect.x >= width - enemySize:
                self.vx = -10
        self.rect.x += self.vx
        self.hitByBall()

    def drawHealthBar(self):
        image1 = pg.Surface((enemyhBarW, enemyhBarH))
        image1.fill(black)
        rect1 = image1.get_rect()
        rect1.x = self.rect.x
        rect1.y = self.rect.y - enemySize / 2 - 5
        self.game.screen.blit(image1, rect1)
        if self.hBarL > 0:
            pg.draw.rect(self.game.screen, blue, (rect1.x, rect1.y, self.hBarL, enemyhBarH))

    def showLostBlood(self):
      if self.hitbyball == True:
        x = self.rect.x
        y = self.rect.y - 80
        font = pg.font.Font("StaySafe-Regular.ttf", 20)
        blood = font.render("hp -" + str(10), True, blue)
        self.game.screen.blit(blood, (x, y))

    def draw(self):
           self.game.screen.blit(self.image, self.rect)
           self.drawHealthBar()
           self.showLostBlood()

# create an inherited class for the boss
class Dragon(Enemy):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = dragonImg
        self.vx = -10
        self.vy = 0
        self.rect.x = x
        self.rect.y = y
        self.distance = 0
        self.blood = 1000
        self.hBarL = 100
        self.attacked = False

    def update(self):
      (x1,y1) = self.game.princess.rect.center
      (x2, y2) = self.rect.center
      self.distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
      if self.distance < width:
        if self.rect.x <= 0:
            self.rect.x = 0
            self.vx = 10
        if self.rect.x >= width:
            self.rect.x = width
            self.vx = -10
        self.rect.x += self.vx
        self.rect.y += self.vy


    def drawHealthBar(self):
        image1 = pg.Surface((100, enemyhBarH))
        image1.fill(black)
        rect1 = image1.get_rect()
        rect1.x = self.rect.x
        rect1.y = self.rect.y - enemySize / 2 - 5
        self.game.screen.blit(image1, rect1)
        if self.hBarL > 0:
            pg.draw.rect(self.game.screen, blue, (rect1.x, rect1.y, self.hBarL, enemyhBarH))

    def showLostBlood(self):
        if self.attacked == True:
            x = self.rect.x
            y = self.rect.y - 80
            font = pg.font.Font("StaySafe-Regular.ttf", 20)
            blood = font.render("hp -" + str(10), True, blue)
            self.game.screen.blit(blood, (x, y))

    def draw(self):
        self.game.screen.blit(self.image, self.rect)
        self.drawHealthBar()
        self.showLostBlood()


    # def fireAttack(self):
    #     self.distance = ((self.rect.x - self.game.princess.rect.x)**2 + (self.rect.y - self.game.princess.rect.y)**2)**0.5
    #     if self.distance < 300:
    #        self.game.attackfire.display = True


class AxeEnemy(Enemy):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = axeEnemyImg
        self.rect.x = x
        self.rect.y = y
        self.blood = 1000
        self.hBarL = bosshBarL
        self.vx = 0
        self.vy = 0
        self.accy = 0
        self.alive = True
        self.attacked = False

    def movement(self):
        self.accy = 1
        self.vy += self.accy
        self.rect.y += self.vy + 0.5 * self.accy

    def isAlive(self):
        if self.attacked == True:
            self.blood -= 20
            self.hBarL -= 20/1000 * bosshBarL
        if self.blood <= 0:
            self.alive = False

    def update(self):
        if self.alive:
            self.isAlive()
            (x, y) = self.rect.centerx, self.rect.centery
            (x1,y1) = self.game.princess.rect.centerx, self.game.princess.rect.centery
            if x1 > self.game.finalplatX:
                xdistance = x - self.game.finalplatX
                vecR = int((y-50)// cellH)
                vecC = int((xdistance) // cellW)
                if (vecR >= 0 and vecR < rows and vecC >= 0 and vecC < cols and Princess.finalMatrix[vecR][vecC] != 0
                        and Princess.finalMatrix[vecR][vecC] != "E"):
                    Princess.finalMatrix = updateMatrixS(Princess.finalMatrix)
                    Princess.finalMatrix[vecR][vecC] = "S"
                    if self.vy == 0:
                        path = solve(Princess.finalMatrix)
                        (targetR, targetC) = path[0]
                        #move toward the platform
                        if targetR == vecR and targetC < vecC:
                            self.vx = -5
                        if targetR == vecR and targetC > vecC:
                            self.vx = 5
                        if targetR < vecR:
                            if targetC < vecC:
                                self.vy = -15
                                self.vx = -5
                            if targetC > vecC:
                                self.vy = -15
                                self.vx = 5
                        if targetR > vecR:
                            if targetC < vecC:
                                self.vx = -5
                            if targetC > vecC:
                                self.vx = 5
                if self.rect.x < self.game.finalplatX:
                    self.rect.x = self.game.finalplatX
                if self.rect.x + 60 - self.game.finalplatX > neWidth:
                    self.rect.x = neWidth + self.game.finalplatX - 60
                if self.rect.y <= 50:
                    self.rect.y = 50
                if self.rect.bottom >= initialBottom:
                    self.rect.bottom = initialBottom
                self.rect.x += self.vx
                self.movement()
            self.hitPlatforoms()


    def hitPlatforoms(self):
            # if the enemy hits the platform, it will stand on the platform
            if self.vy > 0:
                hitPlatform = pg.sprite.spritecollide(self, self.game.finalplatforms, False)
                if hitPlatform:
                    for hit in hitPlatform:
                        # make sure that the enemy will not jump automatically to the platform above when it hits it
                        if self.rect.bottom <= hit.rect.bottom:
                            self.vy = 0
                            self.rect.bottom = hit.rect.top

    def drawHealthBar(self):
        image1 = pg.Surface((bosshBarL, enemyhBarH))
        image1.fill(black)
        rect1 = image1.get_rect()
        rect1.x = self.rect.x - 20
        rect1.y = self.rect.y - 30
        self.game.screen.blit(image1, rect1)
        if self.hBarL > 0:
            pg.draw.rect(self.game.screen, bosshBarCol, (rect1.x, rect1.y, self.hBarL, enemyhBarH))

    def showLostBlood(self):
      if self.attacked == True:
        x = self.rect.x
        y = self.rect.y - 80
        font = pg.font.Font("StaySafe-Regular.ttf", 20)
        blood = font.render("hp -" + str(50), True, red)
        self.game.screen.blit(blood, (x, y))


    def draw(self):
      if self.alive:
        self.game.screen.blit(self.image, self.rect)
        self.drawHealthBar()
        self.showLostBlood()


# create a class for the platform to Jump on

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h, color):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(color)
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
        self.freeze = False


    def drawFrozen(self):
        if self.freeze == True:
            image = freezefireImg
            rect = image.get_rect()
            rect.center = self.rect.center
            self.game.screen.blit(image, rect)

    def draw(self):
        self.game.screen.blit(self.image, self.rect)
        self.drawFrozen()


class FinalFire(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = finalfightImg
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        self.game.screen.blit(self.image, self.rect)


class Fireball(pg.sprite.Sprite):
    def __init__(self, game, enemy):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.enemy = enemy
        self.image = attackfireImg
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)
        self.vx = 0
        self.vy = 0
        self.distance = 0
        self.display = False
        self.shot = False
        self.fire = False
        self.slope = 0
        self.constant = 0
        self.timeElapsed = 0

    def shooting(self):
      if self.enemy.alive == True:
        if self.display == False:
            dt = self.game.clock.tick(fps)
            self.timeElapsed += dt
            if self.timeElapsed > 200:
                self.fire = True
                self.display = True
                self.timeElapsed = 0

    def update(self):
        # can predict movement
        self.distance = ((self.rect.x - self.enemy.rect.x) ** 2 + (self.rect.y - self.enemy.rect.y) ** 2) ** 0.5
        if self.fire == False:
            self.rect.x = self.enemy.rect.x
            self.rect.y = self.enemy.rect.y
        if self.game.x < -(plat5X2 - width):
         self.shooting()
        if self.shot == False and self.fire == True:
            (x1, y1) = self.game.princess.rect.center
            (x2, y2) = self.rect.center
            if x1 != x2:
                s = (y1 - y2) / (x1 - x2)
                c = y1 - s * x1
                self.slope = s
                self.constant = c
                if s > 0:
                    self.vx = 10
                if s < 0:
                    self.vx = -10
            else:
                self.slope = 0
            self.shot = True
        if self.shot == True:
            if self.slope != 0:
                self.rect.x += self.vx
                self.rect.y = self.slope * self.rect.x + self.constant
            if self.slope == 0:
                self.rect.y += 10
            if self.distance > 350:
                self.display = False
                self.fire = False
                self.shot = False


    def draw(self):
        if self.display == True:
            self.game.screen.blit(self.image, self.rect)


class Ball(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = ballImg
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)
        self.vx = 0
        self.vy = 0
        self.distance = 0
        self.distanceEnemy = 0
        self.display = False
        self.slope = 0
        self.constant = 0

    def shooting(self):
        self.display = True
        (x,y) = self.game.mousePos
        (x1,y1) = self.rect.center
        if x != x1:
            self.slope = (y - y1) / (x - x1)
            self.constant = y1 - self.slope * x1
            if x > x1:
                self.vx = 30
            if x < x1:
                self.vx = -30
        else:
            self.slope = 0
            if y < y1:
                self.vy = -5
            if y > y1:
                self.vy = 5

    def update(self):
       if self.game.princess.rect.x > self.game.finalplatX:
            self.image = bigballImg
       (x1,y1) = self.game.princess.rect.center
       (x2,y2) = self.rect.center
       self.distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
       (x3, y3) = self.game.axeEnemy.rect.center
       self.distanceEnemy = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
       if self.distance > 400:
           self.display = False
       if self.display == False:
        self.rect.x = self.game.princess.rect.x + 60
        self.rect.y = self.game.princess.rect.y
       else:
           self.rect.centerx += self.vx
           if self.slope != 0:
             self.rect.centery = self.slope * self.rect.centerx + self.constant
           else:
            self.rect.centery += self.vy
       self.hitEnemy()

    def hitEnemy(self):
       if self.display == True:
        hit1 = pg.sprite.spritecollide(self, self.game.flyingenemies, False)
        if hit1:
                hit1[0].hitbyball = True
                self.display = False
        else:
           for enemy in self.game.flyingenemies:
               enemy.hitbyball = False
        if self.distanceEnemy < 20:
            self.game.axeEnemy.attacked = True
        else:
            self.game.axeEnemy.attacked = False

    def draw(self):
        if self.display == True:
            self.game.screen.blit(self.image, self.rect)


class Axe(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = axeImg
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)
        self.vx = 0
        self.vy = 0
        self.distance = 0
        self.display = False
        self.slope = 0
        self.constant = 0
        self.timeElapsed = 0
        self.dt = 0

    def shooting(self):
        if self.display == False:
            self.dt = self.game.clock.tick(fps)
            self.timeElapsed += self.dt
            if self.timeElapsed > 200:
                self.display = True
                (x, y) = self.game.princess.rect.center
                (x1, y1) = self.rect.center
                if x != x1:
                    self.slope = (y - y1) / (x - x1)
                    self.constant = y1 - self.slope * x1
                    if x > x1:
                        self.vx = 10
                    if x < x1:
                        self.vx = -10
                else:
                    self.slope = 0
                    if y < y1:
                        self.vy = -5
                    if y > y1:
                        self.vy = 5
                self.timeElapsed = 0


    def update(self):
        # can predict movement
      if self.game.axeEnemy.alive == True:
        self.shooting()
        self.distance = ((self.rect.x - self.game.axeEnemy.rect.x) ** 2 + (
                    self.rect.y - self.game.axeEnemy.rect.y) ** 2) ** 0.5
        if self.distance > 200:
            self.display = False
        if self.display == False:
            self.rect.x = self.game.axeEnemy.rect.x
            self.rect.y = self.game.axeEnemy.rect.y
        if self.game.princess.rect.x > self.game.finalplatX:
            self.shooting()
        if self.display == True:
            self.rect.centerx += self.vx
            if self.slope != 0:
                self.rect.centery = self.slope * self.rect.centerx + self.constant
            else:
                self.rect.centery += self.vy
        self.hitPrincess()

    def hitPrincess(self):
        hits = pg.sprite.spritecollide(self, self.game.princesses, False)
        if hits:
            self.game.princess.hitbyAxe = True
            Princess.blood -= 5
            Princess.hBarL -= 5 / princessBlood * princesshBarL
            if hits[0].rect.x < self.rect.x:
                hits[0].vel.x = -2
            if hits[0].rect.x > self.rect.x:
                hits[0].vel.x = 2
            self.display = False
        else:
            self.game.princess.hitbyAxe = False

    def draw(self):
      if self.game.axeEnemy.alive:
        if self.display == True:
            self.game.screen.blit(self.image, self.rect)


class Castle(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = fortressImg
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        self.game.screen.blit(self.image, self.rect)
