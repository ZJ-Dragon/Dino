# DragonDino Ankylosaurus ( v.1.0.23701.1001 )
# This is a Python game developed after imitating Google's Little Dinosaur

import pygame
import random

# 定义一些常量
WINDOW_WIDTH = 800                                              # 窗口宽度
WINDOW_HEIGHT = 500                                             # 窗口高度
DINOSAUR_X = 100                                                # 小恐龙的初始x坐标
DINOSAUR_Y = 400                                                # 小恐龙的初始y坐标
DINOSAUR_SPEED = 0                                              # 小恐龙的初始速度
CACTUS_X = 700                                                  # 仙人掌的初始x坐标
CACTUS_Y = 400                                                  # 仙人掌的初始y坐标
CACTUS_SPEED = -10                                              # 仙人掌的初始速度
score = 0                                                       # 分数

pygame.init()                                                   # 初始化 pygame
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # 创建一个窗口
pygame.display.set_caption('DragonDino Ankylosaurus')           # 设置窗口标题
background = pygame.image.load('Materials/background.png')      # 加载背景图片
dinosaur = pygame.image.load('Materials/dinosaur.png')          # 加载小恐龙图片
cactus = pygame.image.load('Materials/cactus.png')              # 加载仙人掌图片

# 设置小恐龙的位置和速度
dinosaur_x = DINOSAUR_X
dinosaur_y = DINOSAUR_Y
dinosaur_speed = DINOSAUR_SPEED

# 设置仙人掌的位置和速度
cactus_x = CACTUS_X
cactus_y = CACTUS_Y
cactus_speed = CACTUS_SPEED

font = pygame.font.SysFont('arial', 32)              # 创建一个字体对象
clock = pygame.time.Clock()                                     # 创建一个计时器对象
running = True                                                  # 创建一个游戏状态变量

# 游戏主循环
while running:

    screen.fill((255, 255, 255))                                # 填充背景色
    screen.blit(background, (0, 0))                 # 绘制背景图片
    screen.blit(dinosaur, (dinosaur_x, dinosaur_y)) # 绘制小恐龙图片
    screen.blit(cactus, (cactus_x, cactus_y))       # 绘制仙人掌图片

    events = pygame.event.get()                                 # 获取所有的事件

    # 遍历所有的事件
    for event in events:
        # 如果点击了关闭按钮，退出游戏
        if event.type == pygame.QUIT:
            running = False

        # 如果按下了空格键，让小恐龙跳起来
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dinosaur_speed = -17

    dinosaur_y += dinosaur_speed
    dinosaur_speed += 1                                         # 更新小恐龙的位置和速度

    # 如果小恐龙落到地面，让它停在地面上
    if dinosaur_y > DINOSAUR_Y:
        dinosaur_y = DINOSAUR_Y
        dinosaur_speed = DINOSAUR_SPEED

    cactus_x += cactus_speed                                    # 更新仙人掌的位置和速度
    print(cactus_speed)                                            # test

    # 如果仙人掌移出屏幕，让它回到右边重新开始，更新它的速度，并把分数加一
    if cactus_x < -100:
        cactus_x = WINDOW_WIDTH
        score += 1
        cactus_speed = -random.randint(8, 15)

    # 检测小恐龙和仙人掌是否发生碰撞，如果是，结束游戏
    if abs(dinosaur_x - cactus_x) < 50 and abs(dinosaur_y - cactus_y) < 50:
        running = False

        # 创建一个GAME OVER文本对象，并设置颜色为红色和位置为屏幕中央
        game_over = font.render('GAME OVER', True, (0, 0, 0))
        game_over_rect = game_over.get_rect()
        game_over_rect.center = (400, 250)

        # 绘制GAME OVER文本对象到屏幕上，并更新显示
        screen.blit(game_over, game_over_rect)
        pygame.display.flip()

        # 创建一个等待状态变量，并设置为True
        waiting = True

        # 等待用户按下任意键或者关闭按钮再退出游戏的循环
        while waiting:
            # 获取所有的事件
            events = pygame.event.get()

            # 遍历所有的事件
            for event in events:
                # 如果点击了关闭按钮或者按下了任意键，退出等待循环和游戏主循环
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                    waiting = False
                    running = False

    # 显示分数（以仙人掌移动的距离为准）
    score = score + (WINDOW_WIDTH - cactus_x) // 100
    score_text = font.render(str(score), True, (0, 0, 0))
    screen.blit(score_text, (WINDOW_WIDTH - 100, 50))

    pygame.display.flip()                                       # 更新屏幕显示
    clock.tick(60)                                              # 设置每秒帧数为60

pygame.quit()