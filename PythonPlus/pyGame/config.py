class Config:
    target_drop_speed: int
    target_speed_factor: float

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.title = '太空大战'
        self.ship_icon = 'resource/ship.bmp'
        self.ship_speed_factor = 1
        self.ship_limit = 3
        self.bullet_speed_factor = 0.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_max = 3
        self.target_icon = 'resource/alien.bmp'
        self.target_direction = -1  # 1 == right  -1 == left
        self.target_bullet_color = 220, 20, 60
        self.difficulty_increase = 1.1
        self.initDynamicSetting()

    def initDynamicSetting(self):
        self.target_speed_factor = 0.5
        self.target_drop_speed = 50

    def increaseSpeed(self):
        self.target_speed_factor *= self.difficulty_increase
        self.target_drop_speed *= self.difficulty_increase
