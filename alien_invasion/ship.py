import pygame


class Ship:
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')       # 加载飞船图像
        self.rect = self.image.get_rect()       # 返回一个表示飞船的矩形
        self.screen_rect = screen.get_rect()        # 返回一个表示屏幕的矩形

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # self.rect.centery = self.screen_rect.centery

        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)
        # self.centery = float(self.rect.centery)
        self.bottom = float(self.rect.bottom)

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """根据移动标志及飞船rect左右边缘的x坐标调整飞船的位置"""
        # 更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # 飞船上下移动
        if self.moving_up and self.rect.top > 0:
            # self.centery -= self.ai_settings.ship_speed_factor
            self.bottom -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            # self.centery += self.ai_settings.ship_speed_factor
            self.bottom += self.ai_settings.ship_speed_factor

        # 根据self.center更新rect对象
        self.rect.centerx = self.center
        # self.rect.centery = self.centery
        self.rect.bottom = self.bottom
