import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    # 创建配置类Settings的实例
    ai_settings = Settings()
    # print(pygame.display.list_modes())      # 查看本地显示器支持的分辨率
    # 创建名为screen的显示窗口，游戏所有图形元素将在这里绘制，实参(xx, xx)是一个元组，指定窗口的尺寸
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")        # 窗口命名

    # 创建飞船实例
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个用于存储外星人群的编组
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)        # 监听按键和鼠标事件
        ship.update()       # 响应事件，根据移动标志移动飞船
        gf.update_bullets(bullets)      # 响应事件，更新子弹的位置，并删除已出屏幕的子弹
        gf.update_aliens(aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)     # 刷新屏幕


run_game()


