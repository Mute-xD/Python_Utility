import config
import pygame


class Ship:
    def __init__(self, screen):
        self.cfg = config.Config()
        self.screen = screen
        self.image = pygame.image.load(self.cfg.ship_icon)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.movingR = False
        self.movingL = False

    def blitShip(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.movingR and self.rect.right < self.screen_rect.right:
            self.center += self.cfg.ship_speed_factor
        if self.movingL and self.rect.left > 0:
            self.center -= self.cfg.ship_speed_factor
        self.rect.centerx = self.center

    def resetShip(self):
        self.center = self.cfg.screen_width / 2
