import random

# Define the target string
targetString = "HK_Urdahl*__200135"
leastFitIndex = 99999999999999999
# Define genetic algorithm parameters
sizeOfPopulation = 100
mutation_rate = 0.01
crossoverRate = 0.5
indivdsToBeReplcd = 500

# Define the genes (characters) available for the individuals
genes = "abcdefghijklmnopqrstuvwxyzæøåABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789*"

# Function to generate a random individual
def generateIndividual():
    individual = ""
    for _ in range(len(targetString)):
        # Select a random gene from the pool of possible genes
        # Then it gets appended to the individual
        individual += random.choice(genes)
    return individual


# Function to calculate fitness of each individual
def calculateFitness(individual):
    num_matches = 0
    # Loop through each character and check if it is the same as the character,
    # with the same index position, in the
    for a, b in zip(individual, targetString):
        if a == b:
            # If they match, the counter gets incresed
            num_matches += 1
    fitness = num_matches / len(targetString)
    #the maximum fitness score is always going to be one.
    return fitness

# Function to perform crossover
#Link: https://medium.com/@samiran.bera/crossover-operator-the-heart-of-genetic-algorithm-6c0fdcb405c0
def crossoverUniform(parent1, parent2):
    child = ''
    for gene1, gene2 in zip(parent1, parent2):
        if random.random() < crossoverRate:
            child += gene1  #get parent 1 gene
        else:
            child += gene2  #get parent 2 gene
    return child

# Function to perform mutation
def mutate(individual):
    indexOfMutatedInduv = random.randint(0, len(targetString) - 1)
    mutatedGene = random.choice(genes)
    return individual[:indexOfMutatedInduv] + mutatedGene + individual[indexOfMutatedInduv + 1:]

# Initialize the population
population = [generateIndividual() for _ in range(sizeOfPopulation)]

# Evolution loop
generation = 0
while True:
    # Calculate fitness for each individual and puts them in a list
    allFitnessScores = [calculateFitness(individual) for individual in population]


    #print(allFitnessScores)
    #print(population)
    # Finding index of the most fit individual, inside the list
    indexOfBestFit = allFitnessScores.index(max(allFitnessScores))

    #Then using the index of the most fit individual to get the string
    #and then score of that string
    bestFit = population[indexOfBestFit]
    bestFitness = allFitnessScores[indexOfBestFit]

    # results
    print(f"------------------------------------------------------------")
    print(f"The current generation {generation}: ")
    print(f"The best performer has index {indexOfBestFit}")
    print(f"The worst performer has index {leastFitIndex}")
    print(f"The best fit, of the current generation {generation} is {bestFit}")
    print(f"The fitness score of {bestFit} is {bestFitness}")

    # Ending the while-loop if the program found the solution
    if bestFit == targetString:
        print("Solution found!")
        break

    #for ind in range(indivdsToBeReplcd):
    # Select parents based on fitness scores
    # The parents with the best fitness will have the biggest chanse to get selected
    parents = random.choices(population, weights=allFitnessScores, k=2)

    # Perform crossover and mutation to create new individuals
    child = crossoverUniform(parents[0], parents[1])
    child = mutate(child)

    # Replace the least fit individual in the population with the new child
    leastFitIndex = allFitnessScores.index(min(allFitnessScores))
    population[leastFitIndex] = child

    # counter
    generation += 1

    # -> next iteration