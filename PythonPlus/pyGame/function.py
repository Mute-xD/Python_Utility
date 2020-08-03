import sys
import time
import pygame
import bullet
import target


def checkKeyDownEvent(event, cfg, screen, ship, bullets, super_bullets):
    if event.key is pygame.K_d or event.key is pygame.K_RIGHT:
        ship.movingR = True
    if event.key is pygame.K_a or event.key is pygame.K_LEFT:
        ship.movingL = True
    if event.key is pygame.K_SPACE:
        fireBullet(cfg, screen, ship, bullets)
    if event.key is pygame.K_BACKSPACE:
        fireSuperBullet(cfg, screen, ship, super_bullets)
    if event.key is pygame.K_ESCAPE:
        sys.exit()


def checkKeyUpEvent(event, ship):
    if event.key is pygame.K_d:
        ship.movingR = False
    if event.key is pygame.K_a:
        ship.movingL = False


def checkEvent(cfg, screen, ship, bullets, super_bullets, stats, start_button, targets):
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            sys.exit()
        if event.type is pygame.KEYDOWN:
            checkKeyDownEvent(event, cfg, screen, ship, bullets, super_bullets)
        if event.type is pygame.KEYUP:
            checkKeyUpEvent(event, ship)
        if event.type is pygame.MOUSEBUTTONDOWN:
            moues_x, mouse_y = pygame.mouse.get_pos()
            checkPlayButton(stats, start_button, moues_x, mouse_y, targets, bullets, cfg, screen, ship)


def checkPlayButton(stats, play_button, m_s, m_y, targets, bullets, cfg, screen, ship):
    if play_button.rect.collidepoint(m_s, m_y) and stats.game_activate is False:
        stats.game_activate = True
        pygame.mouse.set_visible(False)
        stats.resetStats()
        targets.empty()
        bullets.empty()
        createTargets(cfg, screen, ship, targets, stats)


def updateScreen(screen, cfg, ship, bullets, targets, super_bullets, start_button, stats):
    screen.fill(cfg.bg_color)
    ship.blitShip()
    targets.draw(screen)
    for bullet_ in bullets.sprites():
        bullet_.drawBullet()
    for bullet_ in super_bullets.sprites():
        bullet_.drawBullet()
    if not stats.game_activate:
        start_button.drawButton()
    pygame.display.flip()


def updateBullets(cfg, bullets, targets, super_bullets, screen, ship, stats):
    bullets.update()  # 子弹位置刷新
    super_bullets.update()
    for bullet_ in bullets:
        if bullet_.rect.y <= 0 or bullet_.rect.y >= cfg.screen_height:
            bullets.remove(bullet_)
    for bullet_ in super_bullets:
        if bullet_.rect.y <= 0:
            super_bullets.remove(bullet_)
    # collide_bullet = pygame.sprite.groupcollide(bullets, targets, True, True)
    pygame.sprite.groupcollide(bullets, targets, True, True)
    # 碰撞后子弹消失：True 碰撞后目标消失：True
    # collide_super_bullet = pygame.sprite.groupcollide(super_bullets, targets, False, True)
    pygame.sprite.groupcollide(super_bullets, targets, False, True)
    if len(targets) is 0:
        bullets.empty()
        cfg.increaseSpeed()
        createTargets(cfg, screen, ship, targets, stats)

        print('LEVEL  ', stats.level)


def updateTargets(cfg, targets, ship, stats, bullets, screen):
    isTargetOnEdge(cfg, targets)
    targets.update()
    if pygame.sprite.spritecollideany(ship, targets):
        shipGotHit(stats, targets, bullets, ship, cfg, screen)
    for targets_ in targets:
        if targets_.rect.bottom >= cfg.screen_height:
            shipGotHit(stats, targets, bullets, ship, cfg, screen)
            break


def shipGotHit(stats, targets, bullets, ship, cfg, screen):
    if stats.ship_remain > 0:
        stats.ship_remain -= 1
        print(stats.ship_remain, 'ship left')
        targets.empty()
        bullets.empty()
        ship.resetShip()
        createTargets(cfg, screen, ship, targets, stats)
        time.sleep(0.5)
    else:
        stats.game_activate = False
        pygame.mouse.set_visible(True)


def fireBullet(cfg, screen, ship, bullets):
    if len(bullets) < cfg.bullet_max:
        new_bullet = bullet.Bullet(cfg, screen, ship)
        bullets.add(new_bullet)


def fireSuperBullet(cfg, screen, ship, super_bullets):
    new_super_bullet = bullet.SuperBullet(cfg, screen, ship)
    super_bullets.add(new_super_bullet)


def getNumberTargetsX(cfg, target_width):
    available_space_x = cfg.screen_width - 2 * target_width
    number_target_x = int(available_space_x / (2 * target_width))
    return number_target_x


def createTarget(cfg, screen, targets, target_number, row_number):
    target_ = target.Target(cfg, screen)
    target_width = target_.rect.width
    target_.x = target_width + 2 * target_width * target_number
    target_.rect.x = target_.x
    target_.rect.y = target_.rect.height + 2 * target_.rect.height * row_number
    targets.add(target_)


def createTargets(cfg, screen, ship, targets, state):
    print('create')
    state.levelAdd()
    target_ = target.Target(cfg, screen)
    number_target_x = getNumberTargetsX(cfg, target_.rect.width)
    number_rows = 0
    if number_rows <= getNumberRows(cfg, ship.rect.height, target_.rect.height) and (state.level % 3) is 1:
        print(number_rows, state.level % 3)
        number_rows += 1
    for row in range(number_rows):
        for number in range(number_target_x):
            createTarget(cfg, screen, targets, number, row)


def getNumberRows(cfg, ship_height, target_height):
    available_space_y = (cfg.screen_height - (3 * target_height) - ship_height)
    number_rows = int(available_space_y / (2 * target_height))
    return number_rows


def isTargetOnEdge(cfg, targets):
    for target_ in targets.sprites():
        if target_.isOnEdge():
            changeTargetDirection(cfg, targets)


def changeTargetDirection(cfg, targets):
    for target_ in targets.sprites():
        target_.rect.y += cfg.target_drop_speed
        target_.rect.x -= cfg.target_direction * 10
    cfg.target_direction *= -1
