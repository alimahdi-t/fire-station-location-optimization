from genetic.genetic_algo import genetic_algorithm, fitness
from genetic.visualize import visualize_fitness_map

if __name__ == "__main__":
    best_location = genetic_algorithm()
    print(f"Best location for fire station: {best_location}")
    print(f"Fitness: {fitness(best_location):.2f}")
    print()
    visualize_fitness_map()













