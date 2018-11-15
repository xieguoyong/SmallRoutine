import sys
import pygame
from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按钮按下事件"""
    if event.key == pygame.K_RIGHT:  # 如果按下右箭头，则移动标志置为True，即self.rect.centerx加1
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        # 每按下SPACE键创建一颗子弹，并将其加入到子弹编组中
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """响应按钮松开事件"""
    if event.key == pygame.K_RIGHT:  # 如果松开右箭头，则移动标志置为False
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(ai_settings, screen, ship, bullets):
    """监听、响应按键和鼠标事件"""
    for event in pygame.event.get():    # 通过pygame.event.get()获取事件
        if event.type == pygame.QUIT:   # 通过if语句来检测并响应事件
            sys.exit()      # 检测到pygame.QUIT事件，然后调用sys.exit()响应事件，即退出游戏
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    screen.fill(ai_settings.bg_color)  # 设置背景颜色，每次循环时都重绘屏幕
    ship.blitme()  # 每次循环都重绘飞船
    # 重绘子弹编组中所有子弹
    for bullet in bullets.sprites():      # bullets.sprites()返回一个列表，包含编组bullets中的所有精灵
        bullet.draw_bullet()

    pygame.display.flip()  # 让最近绘制的屏幕可见，实现刷新屏幕



