# colors
green = (52, 168, 84)
yellow = (251, 188, 4)
lightred = (234, 67, 53)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (5, 90, 139)
purple = (117, 80, 166)
finalPlatColor = (5, 0, 139)

# stage size
bgWidth = 1280
stageWidth = bgWidth * 4
stagePosX = 0

# display surface
width = 800
height = 720
fps = 200
hw = width / 2
startScrollingPosX = hw
stopScrolling = stageWidth - hw - startScrollingPosX - 100
playerStatusY = height * 0.1

debugdis = stageWidth - width

# player data
princessWidth = 65
princessHeight = 55
playerAcc = 2
playerFriction = -0.2
playerGravity = 1.8
initialY = 500
initialX = 100
initialBottom = 580
initialCenter = 530
healthBarColor = (255, 78, 78)
princesshBarL = princessWidth + 30
princesshBarH = 10
princessBlood = 500

# platforms data
platformWidth = 100
platformHeight = 15
platformColor = (10, 127, 118)
platxDiff = 200
platyDiff = 80
plat1X = 150
plat1Y = 500
plat2X = plat1X + platxDiff
plat2Y = plat1Y - platyDiff
plat3X = plat2X + platxDiff
plat3Y = plat2Y - platyDiff
plat4X = plat3X + platxDiff
plat4Y = plat2Y
plat5X = plat4X + platxDiff
plat5Y = plat1Y
floorX = 0
floorY = 590

platformList1 = [(plat1X, plat1Y, platformWidth, platformHeight), (plat2X, plat2Y, platformWidth, platformHeight),
                 (plat3X, plat3Y, platformWidth, platformHeight), (plat4X, plat4Y, platformWidth, platformHeight),
                 (plat5X, plat5Y, platformWidth, platformHeight),
                 (floorX, floorY, stopScrolling , platformHeight)]

# enemies data
enemySize = 60
enemyhBarW = enemySize
enemyhBarH = 10
attackValue = 20
bosshBarL = 80
bosshBarCol = (139,1,3)

# score position
scoreX = 50
scoreY = playerStatusY - 10

# rewards data
white = (255, 255, 255)
rewardHeight = 20
rewardWidth = 20
rewardColor = (255, 204, 0)
rewardRadius = 8
rewardList1 = [(plat1X + 20, plat1Y - 30, rewardWidth, rewardHeight, rewardRadius),
               (plat1X + 45, plat1Y - 30, rewardWidth, rewardHeight, rewardRadius),
               (plat2X + 30, plat2Y - 30, rewardWidth, rewardHeight, rewardRadius),
               (plat3X + 30, plat3Y - 30, rewardWidth, rewardHeight, rewardRadius),
               (plat4X + 30, plat4Y - 30, rewardWidth, rewardHeight, rewardRadius),
               (plat4X + 55, plat4Y - 30, rewardWidth, rewardHeight, rewardRadius)]

# rewardIcon
rewardX = scoreX + 150
rewardY = playerStatusY + 10
rewardIcon = (rewardX, rewardY, rewardWidth + 5, rewardHeight + 5, rewardRadius + 5)

# rewardN
rwNumberX = rewardX + 20
rwNumberY = playerStatusY - 10

# healthbar text position
hBarTextX = width / 2
hBarTextY = playerStatusY - 5

# healthbar position
hBarX = hBarTextX + 100
hBarY = playerStatusY
hBarW = width / 3
hBarH = 20

# fire data
fireX1 = plat5X + platformWidth + 300
fireBottom = initialBottom + 10
fireX2 = fireX1 + 300
fireW = 150
fireX3 = fireX2 + 300
fireX4 = fireX3 + 500
fireList = [(fireX1, fireBottom), (fireX2, fireBottom), (fireX3, fireBottom), (fireX4, fireBottom)]

# platform list 2
plat1X2 = fireX2 + 300
plat1Y2 = 500
plat2X2 = plat1X2 + platxDiff
plat2Y2 = plat1Y2 - platyDiff
plat3X2 = plat2X2 + platxDiff
plat3Y2 = plat2Y2 - platyDiff
plat4X2 = plat3X2 + platxDiff
plat4Y2 = plat2Y2
plat5X2 = plat4X2 + platxDiff
plat5Y2 = plat1Y2

platformList2 = [(plat1X2, plat1Y2, platformWidth, platformHeight), (plat2X2, plat2Y2, platformWidth, platformHeight),
                 (plat3X2, plat3Y2, platformWidth, platformHeight), (plat4X2, plat4Y2, platformWidth, platformHeight),
                 (plat5X2, plat5Y2, platformWidth, platformHeight)]

rewardList2 = [(plat1X2 + 20, plat1Y2 - 30, rewardWidth, rewardHeight, rewardRadius),
               (plat1X2 + 45, plat1Y2 - 30, rewardWidth, rewardHeight, rewardRadius),
               (plat2X2 + 30, plat2Y2 - 30, rewardWidth, rewardHeight, rewardRadius),
               (plat3X2 + 30, plat3Y2 - 30, rewardWidth, rewardHeight, rewardRadius),
               (plat4X2 + 30, plat4Y2 - 30, rewardWidth, rewardHeight, rewardRadius),
               (plat5X2 + 55, plat5Y2 - 30, rewardWidth, rewardHeight, rewardRadius)]

plat1X3 = stageWidth - 2 * width - 300
plat1Y3 = 500
plat2X3 = plat1X3 + platxDiff
plat2Y3 = plat1Y3 - platyDiff
plat3X3 = plat2X3 + platxDiff
plat3Y3 = plat2Y3 - platyDiff
plat4X3 = plat3X3 + platxDiff
plat4Y3 = plat2Y3
plat5X3 = plat4X3 + platxDiff
plat5Y3 = plat1Y3

platformList3 = [(plat1X3, plat1Y, platformWidth, platformHeight), (plat2X3, plat2Y3, platformWidth, platformHeight),
                 (plat3X3, plat3Y3, platformWidth, platformHeight), (plat4X3, plat4Y3, platformWidth, platformHeight),
                 (plat5X3, plat5Y3, platformWidth, platformHeight)]

rewardList3 = [(plat1X3 + 20, plat1Y3 - 30, rewardWidth, rewardHeight, rewardRadius),
               (plat1X3 + 45, plat1Y3 - 30, rewardWidth, rewardHeight, rewardRadius),
               (plat2X3 + 30, plat2Y3 - 30, rewardWidth, rewardHeight, rewardRadius),
               (plat3X3 + 30, plat3Y3 - 30, rewardWidth, rewardHeight, rewardRadius),
               (plat4X3 + 30, plat4Y3 - 30, rewardWidth, rewardHeight, rewardRadius),
               (plat5X3 + 55, plat5Y3 - 30, rewardWidth, rewardHeight, rewardRadius)]

matrix = [[0, 1, 0, 1, 0],
          [1, 0, 1, 0, 1],
          [0, 1, 0, 1, 0],
          [1, 0, 1, 0, 1],
          [0, 1, 0, 1, 0],
          ["E", 1, 0, 1, 0]]

matrix2 = [[1, 0, 1, 1, 0],
          [1, 0, 1, 0, 1],
          [0, 1, 0, 1, 1],
          [1, 0, 1, 0, 1],
          [0, "E", 0, 1, 0],
          [1, 1, 0, 1, 0]]

matrix3 = [[1, 0, 1, 0, 1],
          [0, 1, 0, 1, 0],
          [1, 0, 1, 0, 1],
          [0, 1, 0, 1, 0],
          [1, 0, 1, 0, 1],
          ["E", 1, 0, 1, 0]]

matrixes = []
matrixes.append(matrix)
matrixes.append(matrix2)
matrixes.append(matrix3)


rows = len(matrix)
cols = len(matrix[0])
neWidth = width - 256
newHeight = height - 200
cellW = (neWidth) / cols
cellH = (newHeight) / rows
margin = cellW / 5
finalPlatW = cellW - 2 * margin
finalPlatH = 15



margin2 = 2/5*cellW
obstacleW = 1/5*cellW
marginH = 1/5 * cellH
obstacleH = cellH * 3/5
obstacleColor = (109,110,112)


def getObsPos(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                x = cellW * j + margin2 + stageWidth - width
                y = cellH * i + marginH + 50
                result.append((x, y))
    return result

finalObsPos = getObsPos(matrix)

# flying enemies
flyenemyY = 80
flyenemySize = 50

# dragon
dragonSize = 128

# castle
castleSize = 256
castleX = stageWidth - castleSize
castleY = initialBottom - castleSize

# carpet
carpetW = 80
carpetH = 10

# finalfire
finalFirePosX = stageWidth - width
finalFirePosY = 580

# images
# https://www.gameart2d.com/cute-girl-free-sprites.html

# image from: https://www.youtube.com/watch?v=Sv8HPkt-RaY
backgroundImg = "image/background.jpg"
title = "Go Disney Princess"
# image: Icons made by <a href="https://www.flaticon.com/authors/flat-icons" title="Flat Icons">Flat Icons</a>
# from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
castleImg = "image/castle.png"

# sprites
# princess image: <div>Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a>
# from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
princessImg = "image/princess.png"
# enemy image: <div>Icons made by <a href="https://www.flaticon.com/authors/surang" title="surang">surang</a>
# from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
enemyImg = "image/enemy.png"
# quick enemy image: <div>Icons made by <a href="https://www.flaticon.com/authors/surang" title="surang">surang</a>
# from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
quickEnemyImg = "image/fastenemy.png"
# platfrom image: https://www.pixilart.com/art/platform-for-2d-af4f71e97bc8626
platformImg = "image/platform.png"
# source: https://www.pinterest.com/pin/268527196503996164/
mulanImg = "image/mulan.png"
# https://toppng.com/free-image/elsa-magic-frozen-elsa-verano-PNG-free-PNG-Images_177674
elsaImg = "image/elsa.png"
# source: https://www.pngfuel.com/free-png/xpzaa
jasmineImg = "image/jasmine.png"
# source: <div>Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
swordImg = "image/sword.png"
# <div>Icons made by <a href="https://www.flaticon.com/authors/those-icons" title="Those Icons">Those Icons</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
enemySwordImg = "image/enemysword.png"
# Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
fireImg = "image/fire.png"
# Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
flyEnemyImg = "image/flyenemy.png"
# <div>Icons made by <a href="https://www.flaticon.com/authors/pixelmeetup" title="Pixelmeetup">Pixelmeetup</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
iceImg = "image/ice.png"
# <div>Icons made by <a href="https://www.flaticon.com/authors/icongeek26" title="Icongeek26">Icongeek26</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
dragonImg = "image/dragon.png"
# <div>Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
fortressImg = "image/fortress.png"
finalfightImg = "image/finalfight.png"
# Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
attackfireImg = "image/fireball.png"
# Icons made by <a href="https://www.flaticon.com/authors/surang" title="surang">surang</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
axeEnemyImg = "image/boss1.png"
# <div>Icons made by <a href="https://www.flaticon.com/authors/itim2101" title="itim2101">itim2101</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
lifeImg = "image/heart.png"
# Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
freezeImg = "image/freeze.png"
freezefireImg = "image/freezefire.png"
axeImg = "image/axe.png"
#<div>Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
ballImg = "image/circle.png"
#Icons made by <a href="https://www.flaticon.com/authors/pixelmeetup" title="Pixelmeetup">Pixelmeetup</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
bigballImg = "image/dot.png"
#Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
medicineImg = "image/potion.png"
#Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
celebrationImg = "image/rocket.png"
