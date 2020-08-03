import pygame
import config
import function
import ship
import state
import ui
from pygame.sprite import Group


def runGame():
    pygame.init()
    cfg = config.Config()  # config 实例
    screen = pygame.display.set_mode((cfg.screen_width, cfg.screen_height))  # 设置背景

    stats = state.Stats(cfg)
    player_ship = ship.Ship(screen)  # ship 实例
    common_bullets = Group()  # 创建子弹编组
    super_bullets = Group()
    targets = Group()
    # function.createTargets(cfg, screen, player_ship, targets)
    pygame.display.set_caption(cfg.title)
    pygame.display.set_icon(pygame.image.load('resource/ship.bmp'))
    # print('InitSuccess')
    start_button = ui.UI(screen, 'Start')
    while True:
        function.checkEvent(cfg, screen, player_ship, common_bullets, super_bullets, stats, start_button, targets)
        if stats.game_activate:
            player_ship.update()  # 玩家ship位置刷新
            function.updateBullets(cfg, common_bullets, targets, super_bullets, screen, player_ship, stats)
            function.updateTargets(cfg, targets, player_ship, stats, common_bullets, screen)
        function.updateScreen(screen, cfg, player_ship, common_bullets, targets, super_bullets, start_button, stats)


if __name__ == '__main__':
    runGame()
