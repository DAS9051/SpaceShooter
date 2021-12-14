import pygame
 
class TextObject:
 
    def __init__(self, font, position, color, doCenter):
        self.text = font.render("", True, color)
        self.position = position
        self.rect = self.text.get_rect()
        self.color = color
        self.doCenter = doCenter
        if doCenter:
            self.rect.center = (self.position[0] // 2, self.position[1] // 2)
        else:
            self.rect.center = (self.position[0], self.position[1])
 
    def SetValue(self, valueText, font):
        self.text = font.render(valueText, True, self.color)
        self.rect = self.text.get_rect()
        if self.doCenter:
            self.rect.center = (self.position[0] // 2, self.position[1] // 2)
        else:
            self.rect.center = (self.position[0], self.position[1])