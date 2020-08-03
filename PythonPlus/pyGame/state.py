class Stats:
    ship_remain: int

    def __init__(self, cfg):
        self.cfg = cfg
        self.game_activate = False
        self.resetStats()
        self.level = 0

    def resetStats(self):
        self.ship_remain = self.cfg.ship_limit
        self.level = 0

    def levelAdd(self):
        self.level += 1
