import pygame
import sys


def end():
    pygame.init()

    # Установка размеров окна
    screen = pygame.display.set_mode((800, 600))

    # Установка шрифта
    font = pygame.font.Font(None, 36)

    # Создание текста
    text = font.render("Вы выиграли!", True, (0, 0, 0))
    text2 = font.render("Выйти", True, (0, 0, 0))
    # Создание кнопки
    button = pygame.Rect(250, 400, 200, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()
        # Заполнение экрана черным цветом
        screen.fill((255, 255, 255))

        # Отрисовка текста
        screen.blit(text, (250, 200))

        # Отрисовка кнопки

        pygame.draw.rect(screen, [200, 200, 200], button)
        screen.blit(text2, (300, 400))
        # Обновление экрана
        pygame.display.flip()


def endi():
    pygame.init()

    # Установка размеров окна
    screen = pygame.display.set_mode((800, 600))

    # Установка шрифта
    font = pygame.font.Font(None, 36)

    # Создание текста
    text = font.render("Вы проиграли(", True, (0, 0, 0))
    text2 = font.render("Выйти", True, (0, 0, 0))
    # Создание кнопки
    button = pygame.Rect(250, 400, 200, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()
        # Заполнение экрана черным цветом
        screen.fill((255, 255, 255))

        # Отрисовка текста
        screen.blit(text, (250, 200))

        # Отрисовка кнопки

        pygame.draw.rect(screen, [200, 200, 200], button)
        screen.blit(text2, (300, 400))
        # Обновление экрана
        pygame.display.flip()