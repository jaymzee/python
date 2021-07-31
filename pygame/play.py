import pygame
import time

pygame.init()
soundObj = pygame.mixer.Sound('touchtone.wav')
soundObj.play()
time.sleep(2) # wait and let the sound play for 1 second
soundObj.stop()
