import pygame.font

class Scoreboard:
    """report scoring information"""

    def __init__(self, new_game):
        """initialize scoreboard attributes"""
        self.screen = new_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = new_game.settings
        self.stats = new_game.stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # prepare initial score image
        self.prep_score()
    
    def prep_score(self):
        """turn the score into a rendered image"""
        round_score = round(self.stats.score, -1)
        score_str = "Your score is: " + "{:,}".format(round_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # display the score at the top right
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right =self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def show_score(self):
        """draw score on the screen"""
        self.screen.blit(self.score_image, self.score_rect)