from sprites import *
import random


# create a game class
# used the framework from: https://www.youtube.com/watch?v=uWvb3QzA48c&t=1078s

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
        self.timeElapsed = 0
        self.clock = pg.time.Clock()
        self.running = True
        self.gameOver = False
        self.x = 0
        self.allSrpites = pg.sprite.Group()

    def addFire(self):
        self.fires = pg.sprite.Group()
        for pos in fireList:
            (x, y) = pos
            fire = Fire(self, x, y)
            self.fires.add(fire)

    def putEnemies(self):
        self.enemies = pg.sprite.Group()
        for i in range(2):
            enemy = Enemy(self, random.randint(400, 1000), initialCenter)
            self.enemies.add(enemy)
            self.allSrpites.add(enemy)
        for i in range(1):
            quickEnemy = QuickEnemy(self, random.randint(600, 1200), initialCenter)
            self.enemies.add(quickEnemy)
            self.allSrpites.add(quickEnemy)
        for i in range(5):
            flyEnemy = FlyingEnemy(self,random.randint(plat5X2, plat5X2+width-flyenemySize),random.randint(flyenemyY,flyenemyY+100))
            self.enemies.add(flyEnemy)

    def putEnemySwords(self):
        self.enemySwords = pg.sprite.Group()
        for i in range(3):
            enemy = Enemy(self, random.randint(400, 1000), initialCenter)
            self.enemies.add(enemy)
        for i in range(2):
            quickEnemy = QuickEnemy(self, random.randint(600, 1200), initialCenter)
            self.enemies.add(quickEnemy)

    def putPlatforms(self):
        self.platforms = pg.sprite.Group()
        for plat1 in platformList1:
            (x, y, w, h) = plat1
            platform = Platform(x , y, w, h,platformColor)
            self.platforms.add(platform)
            self.allSrpites.add(platform)
        for plat2 in platformList2:
            (x, y, w, h) = plat2
            platform = Platform(x , y, w, h,platformColor)
            self.platforms.add(platform)
        for plat3 in platformList3:
            (x, y, w, h) = plat3
            platform = Platform(x, y, w, h,platformColor)
            self.platforms.add(platform)
        for pos in finalPlatPos:
            (x,y) = pos
            platform = Platform(x, y, finalPlatW, finalPlatH,finalPlatColor)
            self.platforms.add(platform)

    def putRewards(self):
        self.rewards = pg.sprite.Group()
        for rew1 in rewardList1:
            (x, y, w, h, r) = rew1
            reward = Reward(self, x , y, w, h, r)
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

    def new(self):
        # start a new game
        self.x = 0
        self.relX = 0
        # create sprites
        (x, y, w, h, r) = rewardIcon
        self.rewardIcon = Reward(self, x, y, w, h, r)
        self.sword = Sword(self)
        self.addPrincesses()
        self.princess = self.mulan
        self.enemies = pg.sprite.Group()
        self.putPlatforms()
        self.floor = Platform(0, 590, stageWidth, platformHeight,platformColor)
        self.putRewards()
        self.putEnemies()
        self.addFire()
        self.ice = Ice(self)
        self.dragon = Dragon(self,castleX - dragonSize - 50, castleY)
        self.allSrpites.add(self.dragon)
        self.castle = Castle(self, castleX,castleY)
        self.carpet = Carpet(self)
        self.finalfire = FinalFire(self,finalFirePosX, finalFirePosY)
        self.attackfire = Attackfire(self)
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

    def backgroudScrolling(self):
        self.relX = self.x % bgWidth
        if self.x > -width and self.x <= 0:
            if self.princess.pos.x < 30:
                self.princess.pos.x = 30
        if not self.x <= -(stageWidth - startScrollingPosX):
            if self.princess.pos.x > startScrollingPosX:
                self.princess.pos.x = startScrollingPosX
                self.x += -(self.princess.vel.x + 0.5 * self.princess.acc.x)
        else:
            self.princess.pos.x += self.princess.vel.x + 0.5 * self.princess.acc.x
            if self.princess.pos.x >= width:
                self.princess.pos.x = width-30

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

    def enemyAttack(self):
        # if the player is close to the enemies, enemies will attack
        self.dt = self.clock.tick(fps)
        for enemy in self.enemies:
            if enemy.distance < 40:
                enemy.timeElapsed += self.dt
                enemy.move = False
                # attack every 50 frames
                if enemy.timeElapsed > 50:
                   enemy.isAttack = True
                   enemy.attack()
                if enemy.timeElapsed > 70:
                   enemy.isAttack = False
                   self.princess.attacked = False
                   enemy.timeElapsed = 0
            else:
                self.princess.attacked = False
                enemy.move = True

    def isGameOver(self):
        if Princess.blood <= 0:
            self.gameOver = True
            Princess.alive = False

    def updatePlatRewPos(self):
       if not self.x < -(stageWidth -  startScrollingPosX):
        for platform in self.platforms:
            if platform != self.floor:
                platform.rect.x += -(self.princess.vel.x + 0.5 * self.princess.acc.x)
        for reward in self.rewards:
            reward.rect.x += -(self.princess.vel.x + 0.5 * self.princess.acc.x)

    def updateEnemyPos(self):
      if not self.x < -(stageWidth - startScrollingPosX):
        for enemy in self.enemies:
            enemy.rect.x += -(self.princess.vel.x + 0.5 * self.princess.acc.x)

    def update(self):
        # game loop update
        self.clock.tick(fps)
        self.backgroudScrolling()
        self.enemies.update()
        self.fires.update()
        self.platforms.update()
        self.princess.update()
        self.princess.updateMatrix()
        self.sword.update()
        self.mulan.isAttack()
        self.princess.collectReward()
        self.hitPlatform()
        self.enemyAttack()
        self.isGameOver()
        self.updatePlatRewPos()
        self.updateEnemyPos()
        self.ice.update()
        self.princess.hitFire()
        self.dragon.update()
        self.castle.update()
        self.carpet.update()
        self.finalfire.update()
        self.dragon.fireAttack()
        self.attackfire.update()

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

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_r:
                    self.new()
                elif event.key == pg.K_s:
                    self.switchRole()
                elif event.key == pg.K_SPACE:
                    self.princess.jump()
                elif event.key == pg.K_q:
                    self.sword.display = True
                elif event.key == pg.K_w:
                    self.elsa.shoot()
                elif event.key == pg.K_e:
                    if self.jasmine.floating == True:
                        self.jasmine.floating = False
                    else:
                        self.jasmine.floating = True

            if event.type == pg.KEYUP:
                if event.key == pg.K_q:
                    self.sword.display = False
                    self.mulan.attack = False
                elif event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                    self.princess.run = False

    # all the drawing functions

    def drawScrollBg(self):
        background = pg.image.load(backgroundImg).convert()
        bgWidth, bgHeight = background.get_rect().size
        self.screen.blit(background, (self.relX - bgWidth, 0))
        if self.relX < width:
            self.screen.blit(background, (self.relX, 0))

    def showOverScreen(self):
        background = pg.image.load(backgroundImg)
        self.screen.blit(background, ((0, 0)))
        x = width / 2 - 100
        y = height / 2 - 150
        x1 = x - 50
        y1 = y + 100
        font1 = pg.font.Font("StaySafe-Regular.ttf", 100)
        font2 = pg.font.Font("StaySafe-Regular.ttf", 80)
        gameover = font1.render("Game Over", True, (0, 0, 0))
        restart = font2.render("Press 'r' to restart", True, (0, 0, 0))
        self.screen.blit(gameover, (x, y))
        self.screen.blit(restart, (x1, y1))

    def drawEnemyDamage(self):
        hits = pg.sprite.spritecollide(self.mulan, self.enemies, False)
        if hits:
            if self.mulan.attack:
                for hit in hits:
                    hit.showLostBlood()

    def drawRewards(self):
        for reward in self.rewards:
            if reward.rect.x + rewardWidth > 0:
                reward.draw(self.screen)
                reward.drawCircle()

    def showEnemyAttack(self):
        for enemy in self.enemies:
            if enemy.isAttack == True:
                enemy.drawSword()

    def drawHealthBar(self):
        if self.princess.hBarL > 0:
            self.princess.drawHealthBar()
        else:
            self.showOverScreen()

    def drawPrincess(self):
        if self.princess.alive:
            self.princess.draw(self.screen)

    def drawPlatforms(self):
        for platform in self.platforms:
            if platform != self.floor:
                if platform.rect.x + platformWidth > 0:
                    platform.draw(self.screen)

    def drawFire(self):
        for fire in self.fires:
            if fire.rect.x + fireW > 0:
                fire.draw()

    def drawEnemyHBar(self):
        for enemy in self.enemies:
            enemy.drawHealthBar()


    def drawInstruction(self):
        x = 2*width/3 - 50
        y1 = 50
        y2 = y1 + 30
        y3 = y2 + 30
        y4 = y1 - 30
        font = pg.font.Font("StaySafe-Regular.ttf", 35)
        ins1 = font.render("press 'q' for Mulan to attack", True, black)
        ins2 = font.render("press 'w' for Elsa to shoot", True, black)
        ins3 = font.render("press 'f' for Jasmine to fly", True, black)
        ins4 = font.render("press 's' to switch role", True, black)
        self.screen.blit(ins1, (x, y1))
        self.screen.blit(ins2, (x, y2))
        self.screen.blit(ins3, (x, y3))
        self.screen.blit(ins4, (x, y4))



    def draw(self):
        if self.gameOver == False:
            self.drawScrollBg()
            self.castle.draw()
            self.enemies.draw(self.screen)
            self.sword.draw()
            self.drawPlatforms()
            self.drawRewards()
            self.drawPrincess()
            self.carpet.draw()
            self.showEnemyAttack()
            self.princess.drawScore()
            self.rewardIcon.drawCircle()
            self.princess.drawRewardN()
            self.drawHealthBar()
            self.drawFire()
            self.drawEnemyHBar()
            self.princess.showLostBlood()
            self.drawEnemyDamage()
            self.dragon.draw()
            self.ice.draw()
            self.drawInstruction()
            self.finalfire.draw()
            self.attackfire.draw()
        else:
            self.showOverScreen()
        pg.display.update()


# create instance
g = Game()

# main game loop
while g.running:
    g.new()
pg.quit()
