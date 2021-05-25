import numpy as np

class SEIRCellMachine:
    def __init__(self, simulation_time, data_file_name, susceptible, exposed, infective, recovered, exposed_time,
                    infected_time, birth_death_rate, probability_of_getting_disease):
        self.time = 0
        self.simulation_time = simulation_time
        self.density_map = self.read_data(data_file_name)
        self.susceptible = susceptible
        self.exposed = exposed
        self.infective = infective
        self.recovered = recovered
        self.exposed_time = exposed_time
        self.infected_time = infected_time
        # according to paper people are immune to disease after recovery
        # self.recovered_time = recovered_time
        self.birth_death_rate = birth_death_rate
        self.probability_of_getting_disease = probability_of_getting_disease
        self.SEIR_map = []      # contains [S, E, I, R] values for every cell in density map

    def calculate_SEIR_values(self):
        """
        Function calculates SEIR values for every cell in density map
        Should be run every main loop iteration
        :return:
        """
        pass

    def calculate_reproduction_number(self):
        """
        Function calculates reproduction number for every cell in density map
        :return:
        """
        pass

    @staticmethod
    def read_data(file_name):
        with open(file_name) as file:
            lines = file.readlines()
            n_cols = int(lines[0].split(" ")[-1].strip())
            n_rows = int(lines[1].split(" ")[-1].strip())
            xllcorner = lines[2].split(" ")[-1].strip()
            yllcorner = lines[3].split(" ")[-1].strip()
            cell_size = float(lines[4].split(" ")[-1].strip())
            no_data_value = int(lines[5].split(" ")[-1].strip())
            print(f"number of columns: {n_cols}")
            print(f"number of rows: {n_rows}")
            print(f"cell size: {cell_size}")
            print(f"no data value is: {no_data_value}")
            density_map = np.zeros((n_rows, n_cols))
            for row, line in enumerate(lines[6:]):
                for col, density_val in enumerate(line.strip().split(' ')):
                    density_map[row, col] = density_val
            print(f"density map: {density_map}")
            return density_map

    def randomize_board(self):
        """
        Function to randomize density map
        :return:
        """
        pass

    def draw(self, win):
        pass
        # for x in range(self.size):
        #     for y in range(self.size):
        #         if self.board[x][y]:
        #             pygame.draw.rect(win, (255, 0, 0), (x*10, y*10, 10, 10))
        #         else:
        #             pygame.draw.rect(win, (0, 255, 0), (x*10, y*10, 10, 10))
        # pygame.display.update()


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
    # initialize cell machine object
    cell_machine = SEIRCellMachine(300, "polds95ag.asc", S, E, I, R, a, b, birth_death_rate, probs_of_getting_disease)

    # visualization

    # pygame.init()
    # win = pygame.display.set_mode((SIZE*10, SIZE*10))
    # pygame.display.set_caption("Pandemic simulation")
    # run = True
    # while run:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             run = False
    #     cell_machine.draw(win)