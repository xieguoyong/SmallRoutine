class Settings:
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置，可根据自己显示器分辨率调整
        self.screen_width = 1280
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_speed_factor = 1.5

        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 60, 60)
        # self.bullet_allowed = 3         # 限制屏幕上最大子弹数

        # 外星人设置
        self.alien_speed_factor = 1
