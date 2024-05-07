##Declaration of sources:
#The lecture notes from part B in 'Intelligente Systemer'

#Insperation of crossover methods: https://medium.com/@samiran.bera/crossover-operator-the-heart-of-genetic-algorithm-6c0fdcb405c0

#Inspiration for the creation of the fitness function and the mutation functin: https://medium.com/@Data_Aficionado_1083/genetic-algorithms-optimizing-success-through-evolutionary-computing-f4e7d452084f


#No code is directly copied
##
import random
# Defining the target string
targetString = "HK_Urdahl*__200135"
leastFitIndex = 99999999999999999
# Define genetic algorithm parameters
sizeOfPopulation = 100

# Defining the genes which is available for the individuals
genes = "abcdefghijklmnopqrstuvwxyzæøåABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789*"

# Function to generate a random individual
def generateIndividual():
    individual = ""
    for _ in range(len(targetString)):
        # Select a random gene from the pool of possible genes
        # Then it gets appended to the individual
        individual += random.choice(genes)
    return individual
# Function to calculate fitness
def calculateFitness(individual):
    numMatches = 0
    # Loop through each character and check if it is the same as the character,
    # with the same index position, in the
    for a, b in zip(individual, targetString):
        if a == b:
            # If they match, the counter gets incresed
            numMatches += 1
    fitness = numMatches / len(targetString)
    #the maximum fitness score is always going to be one.
    return fitness

# Function to perform crossover
def crossover(parent1, parent2):
    pointOfCrossover = random.randint(0, len(targetString) - 1)
    # Create the child by combining two induvidual parts of the parents
    # The parents has been split at a random point
    child = parent1[:pointOfCrossover] + parent2[pointOfCrossover:]
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

    # Print stats
    print(f"------------------------------------------------------------")
    print(f"The current generation {generation}: ")
    print(f"The best performer has index {indexOfBestFit}")
    print(f"The worst performer has index {leastFitIndex} and is {population[allFitnessScores.index(min(allFitnessScores))]}")
    print(f"The best fit, of the current generation {generation} is {bestFit}")
    print(f"The fitness score of {bestFit} is {bestFitness}")

    # Ending the while-loop if the program found the solution
    if bestFit == targetString:
        print("Solution found!")
        break

    # Select parents based on fitness scores
    parents = random.choices(population, weights=allFitnessScores, k=2)

    # Perform crossover and mutation to create new the individual
    child = crossover(parents[0], parents[1])
    child = mutate(child)

    # Replacing the least fit individual in the population with the new child
    leastFitIndex = allFitnessScores.index(min(allFitnessScores))
    population[leastFitIndex] = child

    # counter
    generation += 1
