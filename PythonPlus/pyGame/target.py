import pygame
from pygame.sprite import Sprite


class Target(Sprite):
    def __init__(self, cfg, screen):
        super(Target, self).__init__()
        self.screen = screen
        self.cfg = cfg
        self.image = pygame.image.load(cfg.target_icon)
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitTarget(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += (self.cfg.target_speed_factor * self.cfg.target_direction)
        self.rect.x = self.x

    def isOnEdge(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        if self.rect.left <= 0:
            return True
