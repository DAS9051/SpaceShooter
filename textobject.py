import pygame
import sys
import os
 
# creats a class for the text
class TextObject:
 
    def __init__(self, font, position, color, doCenter):
        self.text = font.render("", True, color)
        self.position = position
        self.rect = self.text.get_rect()
        self.color = color
        self.doCenter = doCenter
        # this is to easily center the text so I dont need to center it when creating it
        if doCenter:
            self.rect.center = (self.position[0] // 2, self.position[1] // 2)
        else:
            self.rect.center = (self.position[0], self.position[1])


    # this fucntion allows you to easily change the value of the text
    def SetValue(self, valueText, font):

        # renders font and changes color
        self.text = font.render(valueText, True, self.color)

        self.rect = self.text.get_rect()

        # makes sure it is centered when change the value
        if self.doCenter:
            self.rect.center = (self.position[0] // 2, self.position[1] // 2)
        else:
            self.rect.center = (self.position[0], self.position[1])