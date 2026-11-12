"""Reusable gameplay rules for PURPLE HAZE 2.x.

These data-only classes keep quest, creature-bond and enemy rules separate
from the Pygame drawing layer so the Android prototype can grow safely.
"""
class Quest:
    def __init__(self, quest_id, title, description, target=1):
        self.id, self.title, self.description = quest_id, title, description
        self.target = max(1, int(target))
        self.progress = 0
        self.completed = False
        self.claimed = False

    def advance(self, amount=1):
        if self.completed:
            return False
        self.progress = min(self.target, self.progress + max(0, int(amount)))
        self.completed = self.progress >= self.target
        return self.completed

    def claim(self):
        if not self.completed or self.claimed:
            return False
        self.claimed = True
        return True


class CreatureBond:
    """Taming requires repeated calm observation and suitable offerings."""
    def __init__(self, creature_id, name, trust_needed=5):
        self.id, self.name = creature_id, name
        self.trust_needed = max(1, int(trust_needed))
        self.trust = 0
        self.observations = 0
        self.tamed = False

    def observe(self):
        if not self.tamed:
            self.observations += 1
            self.trust = min(self.trust_needed, self.trust + 1)
        return self.trust

    def offer_food(self, suitable=True):
        if self.tamed or not suitable:
            return False
        self.trust = min(self.trust_needed, self.trust + 2)
        self.tamed = self.trust >= self.trust_needed
        return self.tamed


class PatrolEnemy:
    """A small deterministic patrol/damage model; rendering stays in main.py."""
    def __init__(self, enemy_id, x, hp=3, patrol_range=90):
        self.id = enemy_id
        self.x = self.origin_x = float(x)
        self.hp = self.max_hp = max(1, int(hp))
        self.patrol_range = max(10.0, float(patrol_range))
        self.direction = 1
        self.alive = True
        self.hit_cooldown = 0.0

    def update(self, dt, speed=35.0):
        if not self.alive:
            return
        self.x += self.direction * speed * max(0.0, dt)
        if self.x >= self.origin_x + self.patrol_range:
            self.x, self.direction = self.origin_x + self.patrol_range, -1
        elif self.x <= self.origin_x - self.patrol_range:
            self.x, self.direction = self.origin_x - self.patrol_range, 1
        self.hit_cooldown = max(0.0, self.hit_cooldown - max(0.0, dt))

    def damage(self, amount=1):
        if not self.alive or self.hit_cooldown > 0:
            return False
        self.hp = max(0, self.hp - max(1, int(amount)))
        self.hit_cooldown = 0.25
        self.alive = self.hp > 0
        return not self.alive
