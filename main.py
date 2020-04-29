# This file includes tha main game loop


from sprites import *
import random


# create a game class
# used the file organization framework from: https://www.youtube.com/watch?v=uWvb3QzA48c&t=1078s

class Game:
    # initialize the game
    # model
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((width, height))
        # title and icon
        pg.display.set_caption(title)
        icon = pg.image.load(castleImg)
        pg.display.set_icon(icon)
        self.running = True


    def newSetting(self):
        self.running = True
        self.timeElapsed = 0
        self.clock = pg.time.Clock()
        self.running = True
        self.gameOver = False
        self.winning = False
        self.x = 0
        self.allSrpites = pg.sprite.Group()
        self.finalplatX = stageWidth - width
        self.i = 0
        self.matrix = matrix
        self.finalPlatPos = []
        self.mousePos = (0, 0)
        self.intro = True
        self.instruction = False

    def addFire(self):
        self.fires = pg.sprite.Group()
        self.finalfires = pg.sprite.Group()
        for pos in fireList:
            (x, y) = pos
            fire = Fire(self, x, y)
            self.fires.add(fire)
        self.finalfire = FinalFire(self, finalFirePosX, finalFirePosY)
        self.finalfires.add(self.finalfire)

    def putEnemies(self):
        self.enemies = pg.sprite.Group()
        self.flyingenemies = pg.sprite.Group()
        for i in range(4):
            enemy = Enemy(self, random.randint(400, 1000), initialCenter)
            self.enemies.add(enemy)
        for i in range(2):
            quickEnemy = QuickEnemy(self, random.randint(600, 1200), initialCenter)
            self.enemies.add(quickEnemy)
        for i in range(4):
            flyEnemy = FlyingEnemy(self, random.randint(plat5X2, plat5X2 + width - flyenemySize),
                                   random.randint(flyenemyY, flyenemyY + 100))
            self.flyingenemies.add(flyEnemy)
        self.dragon = Dragon(self, plat5X2 + 700, castleY)

    def addFireBall(self):
        self.fireballs = pg.sprite.Group()
        for enemy in self.flyingenemies:
            fireball = Fireball(self, enemy)
            self.fireballs.add(fireball)
        self.dragonfireball = DragonFireball(self, self.dragon)
        self.fireballs.add(self.dragonfireball)

    def putPlatforms(self):
        self.platforms = pg.sprite.Group()
        self.obstacles = pg.sprite.Group()
        for plat1 in platformList1:
            (x, y, w, h) = plat1
            platform = Platform(x, y, w, h, platformColor)
            self.platforms.add(platform)
            self.allSrpites.add(platform)
        for plat2 in platformList2:
            (x, y, w, h) = plat2
            platform = Platform(x, y, w, h, platformColor)
            self.platforms.add(platform)
        for plat3 in platformList3:
            (x, y, w, h) = plat3
            platform = Platform(x, y, w, h, platformColor)
            self.platforms.add(platform)
        self.finalFloor = Platform(castleX, 590, castleSize, platformHeight, platformColor)
        self.platforms.add(self.finalFloor)
        for loc in finalObsPos:
            (x, y) = loc
            obs = Platform(x, y, obstacleW, obstacleH, obstacleColor)
            self.obstacles.add(obs)

    def putRewards(self):
        self.rewards = pg.sprite.Group()
        for rew1 in rewardList1:
            (x, y, w, h, r) = rew1
            reward = Reward(self, x, y, w, h, r)
            self.rewards.add(reward)
            self.allSrpites.add(reward)
        for rew2 in rewardList2:
            (x, y, w, h, r) = rew2
            reward = Reward(self, x, y, w, h, r)
            self.rewards.add(reward)
            self.allSrpites.add(reward)
        for rew3 in rewardList3:
            (x, y, w, h, r) = rew3
            reward = Reward(self, x, y, w, h, r)
            self.rewards.add(reward)
            self.allSrpites.add(reward)

    def addPrincesses(self):
        self.princesses = pg.sprite.Group()
        self.mulan = Mulan(self)
        self.elsa = Elsa(self)
        self.jasmine = Jasmine(self)
        self.princesses.add(self.mulan)
        self.princesses.add(self.elsa)
        self.princesses.add(self.jasmine)
        self.allSrpites.add(self.mulan)
        self.allSrpites.add(self.elsa)
        self.allSrpites.add(self.jasmine)

    def addAxeEnemy(self):
        self.axes = pg.sprite.Group()
        self.axeenemies = pg.sprite.Group()
        self.axe = Axe(self)
        self.axes.add(self.axe)
        self.axeEnemy = AxeEnemy(self, cellW * 3 + margin + stageWidth - width, cellH * 1 + (cellH - finalPlatH) - 64)
        self.axeenemies.add(self.axeEnemy)

    def new(self):
        # start a new game
        self.newSetting()
        self.x = 0
        self.relX = 0
        # create sprites
        (x, y, w, h, r) = rewardIcon
        self.rewardIcon = Reward(self, x, y, w, h, r)
        self.sword = Sword(self)
        self.addPrincesses()
        self.princess = self.mulan
        self.putPlatforms()
        self.putRewards()
        self.putEnemies()
        self.addFire()
        self.addFireBall()
        self.addAxeEnemy()
        self.ice = Ice(self)
        self.ball = Ball(self)
        self.castle = Castle(self, castleX, castleY)
        self.mountain = Mountain(self, plat5X2 + 1.5*width, castleY-130)
        self.carpet = Carpet(self)
        # self.attackfire = Attackfire(self)
        # initialize the game
        self.run()

    # controller
    def run(self):
        # game loop
        while self.running:
            self.clock.tick(fps)
            self.events()
            self.update()
            self.draw()

    def addEnemies(self):
        if len(self.flyingenemies) < 2:
            for i in range(5):
                enemy = FlyingEnemy(self, random.randint(400, 1000), flyenemyY)
                self.flyingenemies.add(enemy)
            for enemy in self.flyingenemies:
                fireball = Fireball(self, enemy)
                self.fireballs.add(fireball)

    def backgroudScrolling(self):
        self.relX = self.x % bgWidth
        if self.x > -(stopScrolling):
            if self.princess.pos.x > startScrollingPosX:
                self.princess.pos.x = startScrollingPosX
                self.x += -(self.princess.vel.x + 0.5 * self.princess.acc.x)
                self.finalplatX += -(self.princess.vel.x + 0.5 * self.princess.acc.x)
        else:
            self.princess.pos.x += self.princess.vel.x + 0.5 * self.princess.acc.x

    def hitPlatform(self):
        # if the player hits the platform, it will stand on the platform
        if self.princess.vel.y > 0:
            hitPlatform = pg.sprite.spritecollide(self.princess, self.platforms, False)
            if hitPlatform:
                for hit in hitPlatform:
                    # make sure that the player will not jump automatically to the platform above when it hits it
                    if self.princess.pos.y <= hit.rect.bottom:
                        self.princess.vel.y = 0
                        self.princess.pos.y = hit.rect.top
            hitFinalPlat = pg.sprite.spritecollide(self.princess, self.finalplatforms, False)
            if hitFinalPlat:
                for hit in hitFinalPlat:
                    # make sure that the player will not jump automatically to the platform above when it hits it
                    if self.princess.pos.y <= hit.rect.bottom:
                        self.princess.vel.y = 0
                        self.princess.pos.y = hit.rect.top

    def enemyAttack(self):
        # if the player is close to the enemies, enemies will attack
        self.dt = self.clock.tick(fps)
        for enemy in self.enemies:
            if enemy.distanceX <= 40 and enemy.distanceY < 10:
                enemy.timeElapsed += self.dt
                enemy.move = False
                enemy.isAttack = True
                enemy.attack()
                if enemy.timeElapsed > 50:
                    enemy.isAttack = False
                    self.princess.attacked = False
                    enemy.timeElapsed = 0

    def isGameOver(self):
        if Princess.alive == False:
            self.gameOver = True

    def buttonPressed(self, mousepos):
        if self.intro:
            (x, y) = mousepos
            posx1 = 1 / 5 * width - 20
            posx2 = 3 / 5 * width -20
            posy = 1 / 2 * height
            if x > posx1 and x < posx1 + buttonW and y > posy and y < posy + buttonH:
                self.intro = False
            if x > posx2 and x < posx2 + buttonW and y > posy and y < posy + buttonH:
                self.intro = False
                self.instruction = True

    def updateSprites(self):
        if self.x > -(stopScrolling):
              if self.princess.pos.x > startScrollingPosX:
                for platform in self.platforms:
                    platform.rect.x += -(self.princess.vel.x + 0.5 * self.princess.acc.x)
                for obstacle in self.obstacles:
                    obstacle.rect.x += -(self.princess.vel.x + 0.5 * self.princess.acc.x)
                for reward in self.rewards:
                    reward.rect.x += -(self.princess.vel.x + 0.5 * self.princess.acc.x)
                for enemy in self.enemies:
                    enemy.rect.x += -(self.princess.vel.x + 0.5 * self.princess.acc.x)
                for enemy in self.flyingenemies:
                    enemy.rect.x += -(self.princess.vel.x + 0.5 * self.princess.acc.x)
                for fire in self.fires:
                    fire.rect.x += -(self.princess.vel.x + 0.5 * self.princess.acc.x)
                self.finalfire.rect.x += -(self.princess.vel.x + 0.5 * self.princess.acc.x)
                self.axeEnemy.rect.x += -(self.princess.vel.x + 0.5 * self.princess.acc.x)
                self.castle.rect.x += -(self.princess.vel.x + 0.5 * self.princess.acc.x)
                self.mountain.rect.x += -(self.princess.vel.x + 0.5 * self.princess.acc.x)
                self.dragon.rect.x += -(self.princess.vel.x + 0.5 * self.princess.acc.x)

    def addFinalPlat(self):
        self.finalplatforms = pg.sprite.Group()
        for pos in self.finalPlatPos:
            (x, y) = pos
            platform = Platform(x, y, finalPlatW, finalPlatH, platformColor)
            self.finalplatforms.add(platform)

    def getPlatPos(self, matrix):
        result = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1 or matrix[i][j] == "E" or matrix[i][j] == "S":
                    x = cellW * j + margin + self.finalplatX
                    y = cellH * i + (cellH - finalPlatH) + 50
                    result.append((x, y))
        return result

    def updateMatrix(self):
        self.matrix = matrixes[self.i]
        self.finalPlatPos = self.getPlatPos(self.matrix)
        self.addFinalPlat()
        dt = self.clock.tick(fps)
        self.timeElapsed += dt
        if self.timeElapsed > 800:
            for plat in self.finalplatforms:
                plat.kill()
            if self.i == 2:
                self.i = 0
            else:
                self.i += 1
            self.timeElapsed = 0

    def win(self):
        if self.princess.pos.x > width - castleSize / 2 and self.axeEnemy.alive == False:
            self.winning = True

    def update(self):
        # game loop update
      if not self.gameOver:
       if not self.instruction and not self.intro:
        self.clock.tick(fps)
        self.isGameOver()
        self.updateMatrix()
        self.backgroudScrolling()
        self.enemies.update()
        self.addEnemies()
        self.flyingenemies.update()
        self.fires.update()
        self.platforms.update()
        self.obstacles.update()
        self.princess.update()
        self.sword.update()
        self.hitPlatform()
        self.enemyAttack()
        self.updateSprites()
        self.ice.update()
        self.dragon.update()
        self.castle.update()
        self.carpet.update()
        self.finalfire.update()
        self.mountain.update()
        # self.dragon.fireAttack()
        self.axeEnemy.update()
        self.axe.update()
        self.ball.update()
        self.fireballs.update()
        self.win()
        # self.attackfire.update()

    # all the event functions

    def switchRole(self):
        if self.princess == self.mulan:
            self.princess = self.elsa
            self.princess.pos = self.mulan.pos
        elif self.princess == self.elsa:
            self.princess = self.jasmine
            self.princess.pos = self.elsa.pos
        elif self.princess == self.jasmine:
            self.princess = self.mulan
            self.princess.pos = self.jasmine.pos
            if self.jasmine.floating == True:
                self.jasmine.floating = False
            if self.jasmine.isfly == True:
                self.jasmine.isfly = False

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.MOUSEBUTTONUP:
                self.mousePos = pg.mouse.get_pos()
                self.buttonPressed(self.mousePos)
                if self.ball.display == False:
                    self.ball.shooting()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.instruction = False
                elif event.key == pg.K_p:
                    self.instruction = True
                elif event.key == pg.K_b:
                    self.instruction = False
                    self.intro = True
                elif event.key == pg.K_r:
                    self.new()
                elif event.key == pg.K_s:
                    self.switchRole()
                elif event.key == pg.K_SPACE:
                    self.princess.jump()
                elif event.key == pg.K_e:
                    if self.jasmine.floating == True:
                        self.jasmine.floating = False
                        self.jasmine.isfly = False
                    else:
                        self.jasmine.floating = True
                        self.jasmine.fly = False
            if event.type == pg.KEYUP:
                if event.key == pg.K_q:
                    self.sword.display = False
                    self.mulan.attack = False
                    for enemy in self.enemies:
                        enemy.attacked = False
                elif event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                    self.princess.run = False

    # all the drawing functions

    def drawScrollBg(self):
        bgWidth, bgHeight = backgroundImg.get_rect().size
        self.screen.blit(backgroundImg, (self.relX - bgWidth, 0))
        if self.relX < width:
            self.screen.blit(backgroundImg, (self.relX, 0))

    def showOverScreen(self):
        self.screen.blit(backgroundImg, ((0, 0)))
        x = width / 2 - 100
        y = height / 2 - 150
        x1 = x - 50
        y1 = y + 100
        font1 = pg.font.Font("fonts/StaySafe-Regular.ttf", 100)
        font2 = pg.font.Font("fonts/StaySafe-Regular.ttf", 80)
        gameover = font1.render("Game Over", True, (0, 0, 0))
        restart = font2.render("Press 'r' to restart", True, (0, 0, 0))
        self.screen.blit(gameover, (x, y))
        self.screen.blit(restart, (x1, y1))

    def drawMainMenu(self):
        if self.intro == True:
            self.screen.blit(castlebackgroundImg, ((0, 0)))
            image = pg.Surface((buttonW, buttonH))
            image.fill(buttonColor)
            rect1 = image.get_rect()
            rect1.x = 1 / 5 * width - 20
            rect1.y = 1 / 2 * height
            self.screen.blit(image, rect1)
            rect2 = image.get_rect()
            rect2.x = 3 / 5 * width -20
            rect2.y = 1 / 2 * height
            self.screen.blit(image, rect2)
            font1 = pg.font.Font("fonts/Choco Bear.otf", 40)
            font2 = pg.font.Font("fonts/Choco Bear.otf", 40)
            start = font1.render("Start", True, black)
            x1 = rect1.x + 60
            y1 = rect1.y + 30
            instruction = font2.render("Instruction", True, black)
            x2 = rect2.x + 20
            y2 = rect2.y + 30
            self.screen.blit(start, (x1, y1))
            self.screen.blit(instruction, (x2, y2))

    def drawInstruction(self):
      if self.instruction:
        self.screen.blit(castlebackgroundImg, ((0, 0)))
        w = 4/5 * width
        h= 4/5 * height + 100
        image = pg.Surface((w, h))
        image.fill(white)
        x = 80
        y = 30
        self.screen.blit(image, ((x,y)))
        x = 140
        y11 = 80
        y = y11 + 50
        y1 = y + 50
        y2 = y1 + 50
        y3 = y2 + 50
        y4 = y3 + 50
        y5 = y4 + 50
        y6 = y5 + 50
        y7 = y6 + 50
        y8 = y7 + 50
        y9 = y8 + 50
        y10 = y9 + 50
        font = pg.font.Font("fonts/KurriIslandPERSONAL-Light.ttf", 25)
        font1 = pg.font.Font("fonts/KurriIslandPERSONAL-Light.ttf", 40)
        inst = font.render("Press 'b' to go back to the main menu", True, black)
        ins = font.render("Press 'p' to pause the game", True, black)
        ins1 = font.render("Press 'esc' to return to the game", True, black)
        ins2 = font.render("Press 'r' to restart the game", True, black)
        ins3= font.render("Press 's' to switch role", True, black)
        ins4 = font.render("Press 'space' to jump", True, black)
        ins5 = font.render("Press 'q' for Mulan to attack", True, black)
        ins6 = font.render("Press 'w' for Elsa to shoot ice", True, black)
        ins7 = font.render("Press 'f' for Jasmine to fly", True, black)
        ins8 = font.render("Press 'e' for Jasmine to float", True, black)
        ins9 = font.render("Press 'e' again for Jasmine to fall down", True, black)
        ins10 = font.render("Click mouse to shoot balls to enemies", True, black)
        self.screen.blit(inst, (x, y11))
        self.screen.blit(ins, (x, y))
        self.screen.blit(ins1, (x, y1))
        self.screen.blit(ins2, (x, y2))
        self.screen.blit(ins3, (x, y3))
        self.screen.blit(ins4, (x, y4))
        self.screen.blit(ins5, (x, y5))
        self.screen.blit(ins6, (x, y6))
        self.screen.blit(ins7, (x, y7))
        self.screen.blit(ins8, (x, y8))
        self.screen.blit(ins9, (x, y9))
        self.screen.blit(ins10, (x, y10))



    def showWinningScreen(self):
            if self.winning:
                self.screen.blit(backgroundImg, ((0, 0)))
                image1 = celebrationImg
                rect1 = image1.get_rect()
                rect1.center = (hw, 2 / 3 * height)
                self.screen.blit(image1, rect1)
                image2 = potionImg
                rect2 = image2.get_rect()
                rect2.center = (hw, 2 / 3 * height)
                self.screen.blit(image2, rect2)
                x = width / 5
                y = height / 6
                x1 = x + 100
                y1 = y + 100
                font1 = pg.font.Font("fonts/StaySafe-Regular.ttf", 100)
                font2 = pg.font.Font("fonts/StaySafe-Regular.ttf", 80)
                congrat = font1.render("Congratulations!", True, (0, 0, 0))
                win = font2.render("You win!", True, (0, 0, 0))
                self.screen.blit(congrat, (x, y))
                self.screen.blit(win, (x1, y1))

    def drawEnemyDamage(self):
        for enemy in self.enemies:
            if enemy.attacked:
                enemy.showLostBlood()

    def drawRewards(self):
        for reward in self.rewards:
            if reward.rect.x + rewardWidth > 0:
                reward.draw(self.screen)
                reward.drawCircle()

    def showEnemyAttack(self):
        for enemy in self.enemies:
            if enemy.isAttack == True:
                enemy.drawSword()

    def drawPrincess(self):
        if Princess.alive:
            self.princess.draw()

    def drawPlatforms(self):
        for platform in self.platforms:
            platform.draw(self.screen)
        for platform in self.finalplatforms:
            platform.draw(self.screen)

    def drawObstacles(self):
        for obstacle in self.obstacles:
            obstacle.draw(self.screen)

    def drawFire(self):
        for fire in self.fires:
            if fire.rect.x + fireW > 0:
                fire.draw()

    def drawEnemyHBar(self):
        for enemy in self.enemies:
            enemy.drawHealthBar()


    def drawLife(self):
        image = lifeImg
        rect = image.get_rect()
        rect.center = (rwNumberX + 70, rwNumberY + 20)
        self.screen.blit(image, rect)
        font = pg.font.Font("fonts/StaySafe-Regular.ttf", 30)
        heart = font.render(f'{Princess.life}', True, black)
        self.screen.blit(heart, (rwNumberX + 100, rwNumberY))

    def drawFreeze(self):
        for enemy in self.enemies:
            if enemy.freeze == True:
                image = freezeImg
                rect = image.get_rect()
                rect.center = enemy.rect.center
                self.screen.blit(image, rect)

    def drawFireBalls(self):
        for fireball in self.fireballs:
            fireball.draw()

    def drawFlyingEnemies(self):
        for enemy in self.flyingenemies:
            enemy.draw()

    def draw(self):
        if self.gameOver == False:
           if self.intro:
             self.drawMainMenu()
           elif self.instruction:
             self.drawInstruction()
           else:
            self.drawScrollBg()
            self.castle.draw()
            self.enemies.draw(self.screen)
            self.drawFlyingEnemies()
            self.drawFreeze()
            self.drawFire()
            self.sword.draw()
            self.drawPlatforms()
            # self.drawObstacles()
            self.drawRewards()
            self.mountain.draw()
            self.drawPrincess()
            self.showEnemyAttack()
            self.rewardIcon.drawCircle()
            self.drawFire()
            self.drawEnemyHBar()
            self.drawEnemyDamage()
            self.dragon.draw()
            self.axeEnemy.draw()
            self.ice.draw()
            self.drawInstruction()
            self.finalfire.draw()
            self.drawFireBalls()
            self.axe.draw()
            self.carpet.draw()
            # self.attackfire.draw()
            self.drawLife()
            self.ball.draw()
            self.showWinningScreen()
        else:
            self.showOverScreen()
        pg.display.update()


# create instance
g = Game()

# main game loop
while g.running:
    g.new()
pg.quit()
