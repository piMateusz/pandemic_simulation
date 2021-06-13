import pygame


class Button:
    def __init__(self, x, y, width, height, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win):
        pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.width, self.height), 2)
        font = pygame.font.SysFont('comicsans', 20)
        text = font.render(self.text, 1, (255, 0, 0))
        win.blit(text, (int(self.x + self.width/2 - text.get_width()/2),
                        int(self.y + self.height/2 - text.get_height()/2)))

    def on_click(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False
