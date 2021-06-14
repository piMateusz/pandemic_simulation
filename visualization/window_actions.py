import pygame
import tkinter
import tkinter.filedialog
import read
import numpy as np


def redraw_window(win, ca, buttons):
    win.fill((100, 100, 100))
    ca.draw_infected(win)
    for button in buttons:
        button.draw(win)
    # ca.draw_density_map(win)
    pygame.display.update()


def select_file():
    """Create a Tk file dialog and cleanup when finished"""
    top = tkinter.Tk()
    top.withdraw()  # hide window
    file_name = tkinter.filedialog.askopenfilename(parent=top)
    top.destroy()
    return file_name


def check_button_click(buttons, pos):
    # action of clicking mouse and reaction on this
    new_density_map = np.float("nan")
    import_data = False
    run_simulation = True
    for counter, button in enumerate(buttons):
        if button.on_click(pos):
            if counter == 0:
                file = select_file()
                new_density_map = read.read_asc(file)
                run_simulation = True
                import_data = True
                print("imported data")
            if counter == 1:
                run_simulation = True
                print("simulation started")
            if counter == 2:
                run_simulation = False
                print("simulation stopped")
            if counter == 3:
                print(f"randomize data")
    return run_simulation, import_data, new_density_map
