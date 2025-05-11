from genetic.genetic_algo import CITY_SIZE, fitness, bridges
import matplotlib.pyplot as plt
import numpy as np


def visualize_fitness_map():
    """
    NOTE: This visualization is only for debugging purpose not presentation.
    :return:
    """
    fitness_map = np.zeros((CITY_SIZE, CITY_SIZE))
    for x in range(CITY_SIZE):
        for y in range(CITY_SIZE):
            fitness_map[y, x] = fitness((x, y))

    print(fitness_map)
    plt.figure(figsize=(8, 8))
    plt.imshow(fitness_map, cmap="viridis", origin="lower")
    plt.colorbar(label="Fitness (Lower is Better)")

    # Plot river
    plt.axhline(4.5, color='blue', linestyle='--', linewidth=2, label='River')

    # Plot bridges
    for bx, by in bridges:
        plt.plot(bx, by, marker='s', color='pink', markersize=10, label='Bridge' if (bx, by) == bridges[0] else "")

    plt.title("Fitness of All Fire Station Locations")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)
    plt.show()