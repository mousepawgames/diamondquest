import pygame

from diamondquest.common import Color
from diamondquest.common import Resolution

from diamondquest.model.player import PlayerModel

class PlayerView(pygame.sprite.Sprite):

    primary = None

    @classmethod
    def get_primary(cls):
        if not cls.primary:
            cls.primary = pygame.sprite.Group(cls())
        return cls.primary

    @classmethod
    def update_view(cls):
        location = PlayerModel.get_player()._location
        cls.primary.update(location)

    def __init__(self):
        super().__init__()
        # TODO start with actual sprite imge
        self.image = pygame.Surface((50, 50))
        self.image.fill(Color.WHITE)
        self.rect = self.image.get_rect()

    def update(self, location):
        # TODO other arguments for animation, setting correct image etc
        # TODO scaling ???
        scale = Resolution.get_primary().block_height  # TODO only valid while display is square
        print('scale', scale)
        self.rect.x = location.col * scale
        self.rect.y = location.row * scale