import pygame


class Fonts:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def fight_panel_font(self):
        font_fight_panel = pygame.font.Font("data\\skyridgesuperital.ttf", self.height // 25)
        return font_fight_panel

    def score_panel_font(self):
        font_score_panel = pygame.font.Font("data\\skyridgesuperital.ttf", self.height // 35)
        return font_score_panel

    def start_header_font(self):
        font_start_header = pygame.font.Font("data\\skyridgegradital.ttf", (self.width // 15))
        return font_start_header

    def start_menu_font(self):
        font_start_menu = pygame.font.Font("data\\skyridgesuperital.ttf", self.width // 46)
        return font_start_menu
