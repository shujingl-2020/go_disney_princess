# colors
green = (52, 168, 84)
yellow = (251, 188, 4)
lightred = (234, 67, 53)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (5, 90, 139)
purple = (117, 80, 166)
finalPlatColor = (137,207,240)

# display surface
width = 800
height = 720
fps = 200
hw = width / 2
startScrollingPosX = hw
playerStatusY = height * 0.1

# stage size
bgWidth = 1280
stageWidth = bgWidth * 4
stagePosX = 0

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
princessBlood = 1000

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
                 (floorX, floorY, stageWidth, platformHeight)]

# enemies data
enemySize = 60
enemyhBarW = enemySize
enemyhBarH = 10
attackValue = 20

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

plat1X3 = stageWidth - width * 2 - 200
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

matrix = [[0, 1, 0, 1, 0, 1],
          [1, 0, 1, 0, 1, 0],
          [0, 1, 0, 1, 0, 1],
          [1, 0, 1, 0, 1, 0],
          [0,  1,  0,  0, 1, 0],
          ["E", 1, 0, 1, "S", 0]]

rows = len(matrix)
cols = len(matrix[0])
cellW = width / cols
cellH = (height-200) / rows
margin = cellW / 5
finalPlatW = cellW - 2 * margin
finalPlatH = 15


def getPlatPos(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                x = cellW * j + margin + stageWidth - width -200
                y = cellH * i + (cellH - finalPlatH) + 50
                result.append((x, y))
    return result


finalPlatPos = getPlatPos(matrix)

# flying enemies
flyenemyY = 80
flyenemySize = 50

# dragon
dragonSize = 128

# castle
castleSize = 256
castleX = stageWidth-castleSize/2
castleY = initialBottom - 110

# carpet
carpetW = 80
carpetH = 10

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
