import random
import math
import numpy as np


# configuration of the problem
CITY_SIZE = 10
POPULATION_SIZE = 100  # number of individuals in each generation
GENERATIONS = 200  # number of generation
MUTATION_RATE = .1  # Mutation rate

# location of bridges
bridges = [(2, 4), (7, 4)]

# Matrix of probability of accident
Matrix = np.array([
    [5, 2, 4, 8, 9, 0, 3, 3, 7, 8],
    [5, 5, 0, 4, 2, 4, 4, 9, 7, 1],
    [9, 3, 4, 2, 7, 8, 9, 7, 8, 4],
    [1, 7, 1, 0, 9, 3, 8, 9, 7, 7],
    [7, 1, 1, 1, 0, 1, 1, 0, 1, 1],  # River not showed in matrix, instead the location of bridges came above
    [4, 7, 4, 0, 7, 0, 0, 9, 0, 8],
    [7, 4, 1, 0, 1, 0, 4, 0, 4, 3],
    [1, 4, 1, 6, 0, 0, 1, 2, 2, 1],
    [5, 1, 5, 9, 6, 3, 6, 6, 2, 5],
    [0, 6, 0, 1, 2, 1, 2, 0, 9, 3]
])


# Calculate the Euclidean distance between two points like (x1, y1) and (x2, y2).
def calc_hypot(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


# Calculates the distance between two points.
def distance(point_1, point_2):
    """
    Calculates the distance between two points.
    If they're on opposite sides of the river, use bridge to cross.
    """
    ax, ay = point_1
    bx, by = point_2
    if (ay < 4 < by) or (ay > 4 > by):
        # Must cross the river — use the shortest path via bridge
        min_bridge = min(
            calc_hypot(ax, ay, bx, by) + calc_hypot(ax, ay, bx, by)
            for bx_, by_ in bridges
        )
        return min_bridge
    else:
        # Doesn't need to cross the river — use the shortest path via bridge
        return calc_hypot(ax, ay, bx, by)


# Creates a random individual (location).
def create_individual():
    return random.randint(0, CITY_SIZE - 1), random.randint(0, CITY_SIZE - 1)


# Applies mutation with a given probability.
def mutate(individual):
    if random.random() < MUTATION_RATE:
        return create_individual()
    return individual


# Creates a child by averaging coordinates of two parents
def crossover(parent1, parent2):
    child_x = (parent1[0] + parent2[0]) // 2
    child_y = (parent1[1] + parent2[1]) // 2
    return child_x, child_y


# select 10 individuals with better Fitness
def select(population):
    population.sort(key=lambda ind: fitness(ind))
    return population[:10]


def genetic_algorithm():
    population = [create_individual() for _ in range(POPULATION_SIZE)]

    for generation in range(GENERATIONS):
        selected = select(population)

        next_generation = []
        while len(next_generation) < POPULATION_SIZE:
            parent1 = random.choice(selected)
            parent2 = random.choice(selected)
            child = crossover(parent1, parent2)
            child = mutate(child)
            next_generation.append(child)

        population = next_generation

    best_station = min(population, key=lambda ind: fitness(ind))
    return best_station


# calculate the fitness for each location to find the best one, The lower fitness is better
def fitness(station):
    total = 0
    for x in range(CITY_SIZE):
        for y in range(CITY_SIZE):
            risk = Matrix[y, x]
            dist = distance(station, (x, y))
            total += risk * dist
    return total

