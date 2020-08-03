import pygame
from pygame.sprite import Sprite


class BulletBase(Sprite):
    def __init__(self, cfg, screen):
        super(BulletBase, self).__init__()
        self.screen = screen
        self.cfg = cfg
        self.speed_factor = cfg.bullet_speed_factor
        self.color = cfg.bullet_color
        self.y = 0.0
        self.rect = None

    def drawRect(self, bullet_width, bullet_height, ship_target, is_ship):
        self.rect = pygame.Rect(0, 0, bullet_width, bullet_height)
        self.rect.centerx = ship_target.rect.centerx
        if is_ship:
            self.rect.top = ship_target.rect.top
        else:
            self.rect.top = ship_target.rect.bottom
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def drawBullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Bullet(BulletBase):
    def __init__(self, cfg, screen, ship):
        super().__init__(cfg, screen)
        self.drawRect(cfg.bullet_width, cfg.bullet_height, ship, True)


class SuperBullet(BulletBase):
    def __init__(self, cfg, screen, ship):
        super().__init__(cfg, screen)
        self.drawRect(300, cfg.bullet_height, ship, True)


class EnemyBullet(BulletBase):
    def __init__(self, cfg, screen, target):
        super().__init__(cfg, screen)
        self.color = cfg.target_bullet_color
        self.drawRect(cfg.bullet_width, cfg.bullet_height, target, False)

    def update(self):
        self.y += self.speed_factor * 0.5
        self.rect.y = self.y
