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

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)        # 监听按键和鼠标事件
        ship.update()       # 响应事件，根据移动标志移动飞船
        bullets.update()        # 将为子弹编组bullets中的每一颗子弹调用bullet.update(）
        gf.update_screen(ai_settings, screen, ship, bullets)     # 刷新屏幕


run_game()


