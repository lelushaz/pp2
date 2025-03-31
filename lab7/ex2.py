import pygame

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((590, 800))


backgrounds = ['images/photo_2025-03-21_21-17-07.jpg',
               'images/photo_2025-03-21_21-19-56.jpg']

songs = ['images/3xKsf9qdS1CyvXSMEid6g8.mp3',
         'images/3cfOd4CMv2snFaKAnMdnvK.mp3']

background_index = 0


bg_image = pygame.image.load(backgrounds[background_index]).convert()
converted_background = pygame.transform.scale(bg_image, (590, 800))
pygame.mixer.music.load(songs[background_index])
pygame.mixer.music.play()

play = False
finish = False

while not finish:
    screen.blit(converted_background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if background_index == len(backgrounds)-1:
                    background_index = 0
                else:
                    background_index = background_index + 1
                bg_image = pygame.image.load(backgrounds[background_index]).convert()
                converted_background = pygame.transform.scale(bg_image, (590, 800))
                pygame.mixer.music.load(songs[background_index])
                pygame.mixer.music.play()

            elif event.key == pygame.K_LEFT:
                if background_index == 0:
                    background_index = len(backgrounds) - 1 
                else:
                    background_index = background_index - 1
                bg_image = pygame.image.load(backgrounds[background_index]).convert()
                converted_background = pygame.transform.scale(bg_image, (590, 800))
                pygame.mixer.music.load(songs[background_index])
                pygame.mixer.music.play()

            elif event.key == pygame.K_SPACE:
                play = not play
                if play:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()

    pygame.display.flip()
