import pygame


def redraw_window(win, ca, buttons):
    win.fill((255, 255, 255))
    ca.draw_infected(win)
    for button in buttons:
        button.draw(win)
    # ca.draw_density_map(win)
    pygame.display.update()


def refresh_window(buttons):
    # action of clicking mouse and reaction on this
    keys = pygame.mouse.get_pressed()
    if keys[0]:         # left mouse button clicked
        x, y = pygame.mouse.get_pos()
        for counter, button in enumerate(buttons):
            # TODO implement on_click actions
            if button.on_click((x, y)):
                print(f"button {counter} clicked !")
