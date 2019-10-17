print('''##################
##Tocando um MP3##
##################''')
print('←→'*30)
import pygame
pygame.mixer.init()
pygame.mixer.music.load(musica.mp3)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
print('→←'*30)
