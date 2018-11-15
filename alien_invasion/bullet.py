import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类"""
    def __init__(self, ai_settings, screen, ship):
        """在飞船所处的位置创建一个子弹对象"""
        super(Bullet, self).__init__()      # 继承Sprite,此为2.7写法，适用于3，也可将括号中的参数去掉
        self.screen = screen

        # 在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
        # 此处因子弹不是基于图像的，必须使用pygame.Rect()类从空白开始创建一个矩形
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx       # 使子弹与飞船矩形处于同一x轴
        self.rect.top = ship.rect.top       # 使子弹顶部与飞船矩形一致，让子弹看起来是从飞船顶部发出的

        # 存储 用小数表示的子弹位置
        self.y = float(self.rect.y)

        # 存储子弹颜色，速度
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        # 更新 表示子弹位置的小数值
        self.y -= self.speed_factor
        # 更新 表示子弹的rect的位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)


