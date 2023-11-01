import pygame
from gui import shapes
def windows():
    grey = (81, 80, 82)
    black = (0, 0, 0)
    size = (600, 660)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Tetris (Dzunisani version)")
    clock = pygame.time.Clock()

    done = False

    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.quit:
                done = True

        screen.fill(black)

        # shapes.o_shape(screen)



        for position in range(0, 650, 30):
            # drawing top to down squares(left
            pygame.draw.rect(screen, (131, 52, 235), (0, position, 30, 30))

            # border drwaing
            pygame.draw.rect(screen, grey, (0, position, 30, 30), width=2)

            # drawing right to left squares(top)
            pygame.draw.rect(screen, (131, 52, 235), (position, 0, 30, 30))

            # border drwaing
            pygame.draw.rect(screen, grey, (position, 0, 30, 30), width=2)

            # drawing top to down squares(on right)
            pygame.draw.rect(screen, (131, 52, 235), (570, position, 30, 30))

            # border drawing
            pygame.draw.rect(screen, grey, (570, position, 30, 30), width=2)

            # drawing right to left squares(bottom)
            pygame.draw.rect(screen, (131, 52, 235), (position ,630, 30, 30))

            # border drwaing
            pygame.draw.rect(screen, grey, (position, 630, 30, 30), width=2)

            # drawing top to down squares(middle)
            pygame.draw.rect(screen, (131, 52, 235), (390, position, 30, 30))

            # border drwaing
            pygame.draw.rect(screen, grey, (390, position, 30, 30), width=2)

            if (position > 390):
                # drawing right to left squares(right)
                pygame.draw.rect(screen, (131, 52, 235), (position, 210, 30, 30))

                # border drwaing
                pygame.draw.rect(screen, grey, (position, 210, 30, 30), width=2)


        def o_shape(screen):
            o_shape_list = [pygame.draw.rect(screen, (131, 52, 235), (90, 90, 30, 30)),
                            # border drwaing
                            pygame.draw.rect(screen, (81, 80, 82), (90, 90, 30, 30), width=2),

                            pygame.draw.rect(screen, (131, 52, 235), (120, 90, 30, 30)),
                            # border drwaing
                            pygame.draw.rect(screen, (81, 80, 82), (120, 90, 30, 30), width=2),

                            pygame.draw.rect(screen, (131, 52, 235), (90, 120, 30, 30)),
                            # border drwaing
                            pygame.draw.rect(screen, (81, 80, 82), (90, 120, 30, 30), width=2),

                            pygame.draw.rect(screen, (131, 52, 235), (120, 120, 30, 30)),
                            # border drwaing
                            pygame.draw.rect(screen, (81, 80, 82), (120, 120, 30, 30), width=2)]


        pygame.display.flip()
        # clock.tick(60)
        black = (0, 0, 0)
    pygame.quit()

    # shapes(screen, grey)

# def shapes(screen, grey):
#
#     shape_a = pygame.draw.rect(screen,grey, 100, 100,30,30)