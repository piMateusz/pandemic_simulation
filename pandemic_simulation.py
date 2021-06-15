#!usr/bin/env python
import time

from ca import CA
import read
from visualization.buttons import Button
import visualization.window_actions as wa
import constants

def main():
    wa.pygame.init()

    # CA
    density_map = read.read_asc("data/polds00g.asc")
    cell_auto = CA(density_map, a=2, b=2, cell_size=constants.CELL_SIZE)

    # screen size
    screen_width = density_map.shape[1] * constants.CELL_SIZE + 200
    screen_height = density_map.shape[0] * constants.CELL_SIZE

    # buttons
    import_data_button = Button(screen_width - 175, 100, 150, 30, "Import data")
    start_simulation_button = Button(screen_width - 175, 200, 150, 30, "Start simulation")
    stop_simulation_button = Button(screen_width - 175, 300, 150, 30, "Stop simulation")
    randomize_data_button = Button(screen_width - 175, 400, 150, 30, "Randomize data")
    buttons = [import_data_button, start_simulation_button, stop_simulation_button, randomize_data_button]

    win = wa.pygame.display.set_mode((screen_width, screen_height))
    wa.pygame.display.set_caption('Pandemic simulation')

    run = True
    run_simulation = True

    # main loop
    while run:

        for event in wa.pygame.event.get():
            if event.type == wa.pygame.QUIT:
                run = False

            if event.type == wa.pygame.MOUSEBUTTONDOWN and event.button == 1:
                run_simulation, import_data, new_density_map = wa.check_button_click(buttons, event.pos)
                if import_data:
                    cell_auto = CA(new_density_map, a=2, b=2, cell_size=constants.CELL_SIZE)

        if run_simulation:
            wa.redraw_window(win, cell_auto, buttons)
            cell_auto.run(1)

        time.sleep(0.1)

    wa.pygame.quit()
