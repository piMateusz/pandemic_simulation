import pygame
from constants import *
import random


class SIRCellMachine:
    def __init__(self, size, infection_time, recover_time, time, people_infected):
        self.size = size
        self.infection_time = infection_time
        self.recover_time = recover_time
        self.board = [[0 for _ in range(size)] for _ in range(size)]
        self.time = time
        self.people_infected = people_infected
        self.randomize_board()

    def randomize_board(self):
        for x in range(self.people_infected):
            rand_row = random.randint(0, self.size-1)
            rand_col = random.randint(0, self.size-1)
            while self.board[rand_row][rand_col]:
                rand_row = random.randint(0, self.size-1)
                rand_col = random.randint(0, self.size-1)
            self.board[rand_row][rand_col] = 1

    def draw(self, win):
        for x in range(self.size):
            for y in range(self.size):
                if self.board[x][y]:
                    pygame.draw.rect(win, (255, 0, 0), (x*10, y*10, 10, 10))
                else:
                    pygame.draw.rect(win, (0, 255, 0), (x*10, y*10, 10, 10))
        pygame.display.update()

#     def update_machine(self):
#         temp_board = self.board
#         for x in range(self.size):
#             for y in range(self.size):
#                 if not self.board[x][y]:
#                     for i in range(-1, 2):
#                     for j = -1: 1
#                     if (0 < i + row & & i + row < n)
#                         if (0 < j + col & & j + col < n)
#                             if (0 < D(row + i, col + j) & & D(row + i, col + j) <= a)
#                                 temp_D(row, col) = 1;
#                             end
#                         end
#                     end
#                 end
#             end
#         elseif(D(row, col) < a + b)
#         temp_D(row, col) = D(row, col) + 1;
#
#     else
#     temp_D(row, col) = 0;
#
#
# end


if __name__ == "__main__":
    cell_machine = SIRCellMachine(SIZE, INFECTION_TIME, RECOVER_TIME, TIME, PEOPLE_INFECTED)
    pygame.init()
    win = pygame.display.set_mode((SIZE*10, SIZE*10))
    pygame.display.set_caption("Pandemic simulation")
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        cell_machine.draw(win)