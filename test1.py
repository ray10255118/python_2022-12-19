import pygame


def main():
    # Settings
    width = 600
    height = 400
    color_background = (30, 30, 30)
    color_font = (200, 200, 200)

    # Init
    pygame.init()
    window_size = (width, height)
    screen = pygame.display.set_mode(window_size)

    # Text
    font = pygame.font.SysFont("Arial", 35)
    text = font.render("Hello World", True, color_font)
    text_rect = text.get_rect(center=(width/2, height/2))

    # Run
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Fills
        screen.fill(color_background)
        screen.blit(text, text_rect)

        # Updates
        pygame.display.update()


if __name__ == "__main__":
    main()