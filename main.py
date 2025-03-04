import numpy as np
import matplotlib.pyplot as plt
import math

class Traffic:

    def __init__(self, number_of_cells, number_of_iterations, car_density):
        self.road_length = number_of_cells
        self.total_time_step = number_of_iterations
        self.density = car_density
        self.road_grid = [np.zeros(number_of_cells, dtype=int).tolist()]
        self.actual_cars = 0
        self.cars_moved = 0
        self.average_speed = 0

        # takes empty grid of zeros and populates with cars in relation to 
        # input density
        for index in range(len(self.road_grid[0])):
            random_number = np.random.rand()
            if self.density >= random_number:
                self.actual_cars += 1
                self.road_grid[0][index] = 1
        print(self.road_grid)

        self.actual_density = round(self.actual_cars / number_of_cells, 2)
        print(f"Experimental Car Density: {self.actual_density}")
        print(f"Numbers of Cars: {self.actual_cars}")

    def __str__(self):
        s = ""
        for row in self.road_grid:
            for point in row:
                s+= f"{point}"
            s += "\n"
        return s



    def move_cars_one_step(self):
        """
        function to move cars forwards if space is free
        """

        # copy last row of self.road grid and modify to include updated halo
        copy_last_row = self.road_grid[-1].copy()

        #print(f"{copy_last_row} copy_last_row")

        #adds zeros to both ends
        copy_last_row.insert(0,0)
        copy_last_row.append(0)

        #print(f"{copy_last_row} copy_last_row")

        # checks LH inner cell to update RH halo
        if copy_last_row[1] == 1:
            copy_last_row[-1] = 1
        #print(f"{copy_last_row} LH inner update RH cell")

        # checks RH inner cell to update LH halo
        if copy_last_row[-2] == 1:
            copy_last_row[0] = 1
        #print(f"{copy_last_row} RH inner update LH cell")
        
        #print(f"{self.road_grid} self.road_grid")
        #print(f"{copy_last_row} copy_last_row updated halo")

        updated_road = [0] * len(copy_last_row)
        #print(f"{updated_road} updated road")

        cars_moved = 0
        
        for index, space in enumerate(copy_last_row):

            # ignore last item in array (RH halo)
            if index == len(copy_last_row) -1:
                break

            #print(f"{index}")

            #print(f"{copy_last_row} copy_last_row loop {index}")
            if space == 1:
                #if the space in front is occupied then remain stationary
                if copy_last_row[index + 1] == 1:
                    updated_road[index] = 1
                else:
                    updated_road[index] = 0
                    if index != 0: 
                        cars_moved += 1
            else:
                #if the space behind has car then move it forward
                if copy_last_row[index -1] == 1:
                    updated_road[index] = 1
                else:
                    updated_road == 0

        self.cars_moved = cars_moved
        self.average_speed = self.cars_moved / self.actual_cars \
        #    if self.actual_cars != 0 else 0

        # remove values from either end of updated list
        updated_road.pop(0)
        updated_road.pop(-1)
        
        self.road_grid.append(updated_road)

        return self.cars_moved

    def move_cars(self):
        """
        calls the move_cars_one_step() function by the amount specified
        """
        for index in range(self.total_time_step):
            self.move_cars_one_step()
            print(
                f"Timestep: {index},  "
                f"Cars Moved: {self.cars_moved}, "
                f"Average Speed: {self.average_speed}"
            )
        

def main():

    print("Traffic Simulation utilising cellular automata, Insert values for : ")

    # while True:
    #     try:
    #         number_of_cells = int(input("Road length (Number of Cells): "))
    #         if number_of_cells <= 0:
    #             print("Error: Road length must be a positive integer. Please try again.")
    #             continue
    #         break
    #     except ValueError:
    #         print("Error: Invalid input. Please enter a valid integer.")

    # while True:
    #     try:
    #         number_of_iterations = int(input("Number of Iterations (Number of Timesteps): "))
    #         if number_of_iterations <= 0:
    #             print("Error: Number of iterations must be a positive integer. Please try again.")
    #             continue
    #         break
    #     except ValueError:
    #         print("Error: Invalid input. Please enter a valid integer.")

    # while True:
    #     try:
    #         car_density = float(input("Car Density (0 < x < 1): "))
    #         if car_density <= 0 or car_density >= 1:
    #             print("Error: Car density must be a number between 0 and 1. Please try again.")
    #             continue
    #         break
    #     except ValueError:
    #         print("Error: Invalid input. Please enter a valid number.")

    print("Simulation parameters set successfully!")

    number_of_cells = 20
    number_of_iterations = 20
    car_density = 0.5

    traffic_model = Traffic(number_of_cells, number_of_iterations, car_density)
    print(traffic_model)

    traffic_model.move_cars()
    print(traffic_model)

if __name__ == "__main__":
    main()