import numpy as np
import matplotlib.pyplot as plt
import math

class Traffic:

    def __init__(self, number_of_cells, number_of_iterations, car_density):
        self.road_length = number_of_cells
        self.total_time_step = number_of_iterations
        self.density = car_density
        #initialise 1D grid of "cars" using the given parameters 
        #append new iterations to grid, starting with initial 1D grid
        # grid has empty zeros at each end- halo region- in this example 
        # self.road_length is 6
        self.road_grid = [[0, 0, 0, 1, 0, 1, 1, 0]]
        # copy of list with halo looks like [1, 0, 0, 1, 0, 1, 1, 0]

    def __str__(self):
        s = ""
        for row in self.grid:
            for point in row:
                s+= f"{point}"
            s += "\n"
        return s

    """
    function to move cars forwards if space is free
    """

    def move_car(self):

        #first find out if there are cars at either end of the road
        #and copy them to a new list
        
        # list that user sees [0, 0, 1, 0, 1, 1]
        # init list     =  [0, 0, 0, 1, 0, 1, 1, 0]
        # function inside init determines the new halo list for each iteration
        # halo list     =  [1, 0, 0, 1, 0, 1, 1, 0]
        # halo list is ready to be updated with move_car()
        # new list      =  [0, 1, 0, 0, 1, 1, 0, 0]

        # copy last row of self.road grid and modify to include updated halo
        copy_last_row = self.road_grid[-1]

        # checks LH inner cell to update RH halo
        if copy_last_row[1] == 0:
            copy_last_row[-1] = 1
        # checks RH inner cell to update LH halo
        if copy_last_row[-2] == 1:
            copy_last_row[0] = 1
        

        """
        
        for index, space in self.road_grid:

            # skips the halo region
            if index == 0 or -1:
                continue

            if space == 1:
                #if the space in front is occupied then remain stationary
                if self.road_grid[index + 1] == 1:
                    space = 1
                else:
                    space = 0

        """


        self.road_grid.append([0, 0, 0, 1, 0, 1, 1, 0])
        print(self.road_grid)

def main():

    number_of_cells = 6
    number_of_iterations = 5
    car_density = 0.5

    traffic_model = Traffic(number_of_cells, number_of_iterations, car_density)

    traffic_model.move_car()
    print(traffic_model)

if __name__ == "__main__":
    main()