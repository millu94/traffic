import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import math

class Traffic:

    def __init__(self, number_of_cells, number_of_iterations, car_density):
        self.total_time_step = number_of_iterations
        self.density = car_density
        self.road_grid = [np.zeros(number_of_cells, dtype=int).tolist()]
        self.actual_cars = 0
        self.cars_moved = 0
        self.average_speed = 0
        self.steady_state_average = 0

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

        # adds zeros to both ends
        copy_last_row.insert(0,0)
        copy_last_row.append(0)

        # checks LH inner cell to update RH halo and vice versa
        if copy_last_row[1] == 1:
            copy_last_row[-1] = 1

        if copy_last_row[-2] == 1:
            copy_last_row[0] = 1

        # creates an empty road of zeros
        updated_road = [0] * len(copy_last_row)

        cars_moved = 0
        
        for index, space in enumerate(copy_last_row):

            # ignore last item in array (RH halo)
            if index == len(copy_last_row) -1:
                break

            if space == 1:
                # if the space in front is occupied then remain stationary
                if copy_last_row[index + 1] == 1:
                    updated_road[index] = 1
                else:
                    updated_road[index] = 0
                    # ignores LH halo region as car moving from RH inner 
                    # will add to total for cars_moved
                    if index != 0: 
                        cars_moved += 1
            else:
                # if the space behind has car then move it forward
                if copy_last_row[index -1] == 1:
                    updated_road[index] = 1
                else:
                    updated_road == 0

        self.cars_moved = cars_moved
        # when cars_moved = actual cars consistently, steady state average
        self.average_speed = self.cars_moved / self.actual_cars \
            if self.actual_cars != 0 else 0

        # remove halo values from either end of updated list
        updated_road.pop(0)
        updated_road.pop(-1)
        
        self.road_grid.append(updated_road)

    def move_cars(self, print_option):
        """
        calls the move_cars_one_step() function by the amount specified, 
        returns steady state average as average speed for final timestep
        """
        for index in range(self.total_time_step):
            self.move_cars_one_step()
            if print_option == 1:
                print(
                    f"Timestep: {index + 1},  "
                    f"Cars Moved: {self.cars_moved}, "
                    f"Average Speed: {round(self.average_speed, 2)}"
                )
        self.steady_state_average = self.average_speed
        print(
            f"Steady State Average Speed: "
            f"{round(self.steady_state_average, 2)}"
        )
        

def main():

    print("Traffic Simulation utilising cellular automata, Insert values for"
        ": ")

    while True:
        try:
            number_of_cells = int(input("Road length (Number of Cells): "))
            if number_of_cells <= 0:
                print("Error: Road length must be a positive integer. Please "
                      "try again."
                )
                continue
            break
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")

    while True:
        try:
            number_of_iterations = int(
                input("Number of Iterations (Number of Timesteps): ")
                )
            if number_of_iterations <= 0:
                print("Error: Number of iterations must be a positive integer"
                      ". Please try again.")
                continue
            break
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")

    # ask user either rum simulation for particular density or all densities

    print("Would you like to run simulation for a particular density or a "
          " range of densities?")

    while True:
        try:
            user_choice = int(
                input("Enter 1 for particular density, 2 for range: ")
                )
            if user_choice == 1:
                while True:
                    try:
                        car_density = float(
                            input("Car Density (0 < x < 1): ")
                            )
                        if 0 < car_density < 1:
                            break
                        else:
                            print("Error: Car density must be a number "
                                  " between 0 and 1. Please try again.")
                    except ValueError:
                        print("Error: Invalid input. Please enter a valid " 
                              " number.")
                break
            elif user_choice == 2:
                # set car density equal to 5 for default grid and calculate 
                # range
                """
                insert function call here

                create a range of densities between 0 and 1

                for each density create an object using number of cells and 
                number of iterations inputted by user

                call move_cars() on each object
                """
                densities = np.arange(0.1, 1, 0.01)
                actual_densities = []
                steady_vs_density = []
                print(densities)
                for density in densities:
                    traffic_model = Traffic(
                        number_of_cells, number_of_iterations, density
                    )
                    traffic_model.move_cars(0)
                    if traffic_model.actual_density != 0:
                        actual_densities.append(traffic_model.actual_density)
                        steady_vs_density.append(
                            traffic_model.steady_state_average
                        )
                    
                    print(traffic_model.actual_density)
                    print(traffic_model.steady_state_average)

                print(actual_densities)
                print(steady_vs_density)

                plt.plot(actual_densities, steady_vs_density)
                plt.xlabel("Densities")
                plt.ylabel("Steady State Average Speed")
                plt.show()

                car_density = 0.5
                break
            else:
                print("Error: Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")


    print("Simulation parameters set successfully!")

    # number_of_cells = 20
    # number_of_iterations = 20
    # car_density = 0.5


    """
    Default object creation that will happen for either: option 1 (user 
    specifies one density) or option 2 will set density equal to 0.5 and
    make the same graph, and output range of densities to separate graph
    """
    traffic_model = Traffic(
        number_of_cells, number_of_iterations, car_density
    )
    print(traffic_model)

    traffic_model.move_cars(1)
    print(traffic_model)

    colors = ['blue', 'yellow']  # blue = space, yellow = car
    cmap = mcolors.ListedColormap(colors)

    fig, ax = plt.subplots(figsize=(10, 10))

    im = ax.imshow(
        traffic_model.road_grid, interpolation='none', origin='lower', \
        cmap=cmap, vmin=0, vmax=1
    )
    
    ax.set_xticks(range(number_of_cells))  
    ax.set_xticklabels(range(number_of_cells))  

    ax.set_yticks(range(number_of_iterations))  
    ax.set_yticklabels(range(number_of_iterations)) 

    cbar = plt.colorbar(im, ax=ax, ticks=[0.25, 0.75])
    cbar.ax.set_yticklabels(['Space', 'Car'])

    plt.title("Traffic Model Road Grid")
    plt.xlabel("Car Position")
    plt.ylabel("Timestep")

    textstr = (
        f"Experimental Car Density: {traffic_model.actual_density:.2f}\n"
        f"Number of Cars: {traffic_model.actual_cars}\n" 
        f"Steady State Average : {traffic_model.steady_state_average}"
    )
    fig.text(0.02, 0.95, textstr, fontsize=10, color="black",
         verticalalignment='top', horizontalalignment='left',
         bbox=dict(
             boxstyle="round,pad=0.3", edgecolor='black', facecolor='white'))


    plt.tight_layout()

    plt.show()

if __name__ == "__main__":
    main()