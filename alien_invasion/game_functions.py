import sys
import pygame
from bullet import Bullet
from alien import Alien


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
    elif event.key == pygame.K_SPACE:       # 按空格键射击
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_ESCAPE:      # 按ESC键退出游戏
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
    """每按下SPACE键创建一颗子弹，并将其加入到子弹编组中"""
    # if len(bullets) < ai_settings.bullet_allowed:       # 限制屏幕中子弹数量
    #     new_bullet = Bullet(ai_settings, screen, ship)
    #     bullets.add(new_bullet)
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


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    screen.fill(ai_settings.bg_color)  # 设置背景颜色，每次循环时都重绘屏幕
    ship.blitme()  # 每次循环都重绘飞船
    aliens.draw(screen)  # 每次循环都重绘外星人群
    # 重绘子弹编组中所有子弹
    for bullet in bullets.sprites():      # bullets.sprites()返回一个列表，包含编组bullets中的所有精灵
        bullet.draw_bullet()

    pygame.display.flip()  # 让最近绘制的屏幕可见，实现刷新屏幕


def update_bullets(bullets):
    """更新所有子弹的位置，并删除已出屏幕的子弹"""
    # 更新子弹的位置。将为子弹编组bullets中的每一颗子弹调用bullet.update(）
    bullets.update()

    # 删除出了屏幕的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))


def get_number_aliens_x(ai_settings, alien_width):
    """计算每行可容纳多少个外星人"""
    # 屏幕两边预留一个外星人宽度的空白区，外星人间距为一个外星人宽度
    # 去除屏幕两边预留的空白区后剩余的宽度
    available_space_x = ai_settings.screen_width - 2*alien_width
    # 外星人数量=剩余宽度/（一个外星人宽度+中间间距（即一个外星人宽度）），并取整
    number_aliens_x = int(available_space_x/(2*alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可容纳多少行外星人"""
    # 屏幕顶部预留一个外星人高度的空白区，行间距为一个外星人高度
    # 去除顶部空白区，去除第一行外星人+第一行间距，去除飞船的高度
    available_space_y = ai_settings.screen_height - 3*alien_height - ship_height
    # 可容纳行数=剩余高度/（外星人高度+行间距），并取整
    number_rows = int(available_space_y/(2*alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人并将其放在当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + 2 * alien_width * alien_number  # 设置每个外星人在当前行的位置
    alien.rect.x = alien.x
    alien.rect.y = alien_height + 2*alien_height*row_number
    aliens.add(alien)  # 将每个外星人加入到编组


def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    for row_number in range(number_rows):
        for number_alien in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, number_alien, row_number)


def update_aliens(aliens):
    """更新外星人群中所有外星人的位置"""
    aliens.update()
