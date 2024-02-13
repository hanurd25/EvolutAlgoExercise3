import random

# Define the target string
target_string = "HK_Urdahl*__200135"

# Define genetic algorithm parameters
population_size = 100
mutation_rate = 0.01

# Define the genes (characters) available for the individuals
genes = "abcdefghijklmnopqrstuvwxyzæøåABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789*"

# Function to generate a random individual
def generate_individual():
    return ''.join(random.choice(genes) for _ in range(len(target_string)))

# Function to calculate fitness
def calculate_fitness(individual):
    return sum(1 for a, b in zip(individual, target_string) if a == b) / len(target_string)

# Function to perform crossover
def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(target_string) - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

# Function to perform mutation
def mutate(individual):
    mutated_index = random.randint(0, len(target_string) - 1)
    mutated_gene = random.choice(genes)
    return individual[:mutated_index] + mutated_gene + individual[mutated_index + 1:]

# Initialize the population
population = [generate_individual() for _ in range(population_size)]

# Evolution loop
generation = 0
while True:
    # Calculate fitness for each individual
    fitness_scores = [calculate_fitness(individual) for individual in population]

    # Find the best fit individual
    best_fit_index = fitness_scores.index(max(fitness_scores))
    best_fit = population[best_fit_index]
    best_fitness = fitness_scores[best_fit_index]

    # Print current generation and best fit
    print(f"Generation {generation}: Best fit - {best_fit}, Fitness - {best_fitness}")

    # Terminate if the solution is found
    if best_fit == target_string:
        print("Solution found!")
        break

    # Select parents based on fitness scores
    parents = random.choices(population, weights=fitness_scores, k=2)

    # Perform crossover and mutation to create new individuals
    child = crossover(parents[0], parents[1])
    child = mutate(child)

    # Replace the least fit individual in the population with the new child
    least_fit_index = fitness_scores.index(min(fitness_scores))
    population[least_fit_index] = child

    # Increment generation counter
    generation += 1
