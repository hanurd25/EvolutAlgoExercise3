import matplotlib.pyplot as plt
import random
import numpy as np

# Define the target string
targetString = "HK_Urdahl*__250201"
leastFitIndex = 99999999999999999
# Define genetic algorithm parameters
sizeOfPopulation = 1000
mutationRate = 0.07
crossoverRate = 0.5
indivdsToBeReplcd = 500

bestPerformers = [] #List for holding the best performer for every generation
averageFitness = [] #List for holding the average fitness for every generation
medianFitness = [] #List for holding the median fitness for every generation
childFitness= [] #List for holding the fitness for children for every generation

# Possible genes available
genes = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789*"

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
    # with the same index position, in the solution string
    for a, b in zip(individual, targetString):
        if a == b:
            # If they match, the counter gets incresed
            num_matches += 1
    fitness = num_matches / len(targetString)
    #the maximum fitness score is always going to be one.
    return fitness

# Function to perform crossover
def crossoverUniform(parent1, parent2):
    child = '' #initialize the child as an emety string.
    for gene1, gene2 in zip(parent1, parent2):
        if random.random() < crossoverRate:
            child += gene1  #get gene from parent 1
        else:
            child += gene2  #get gene from parent 2
    return child

# Function to perform mutation
def mutate(individual): #One gene in the offspring is being replaced with a random gene
    indexOfMutatedInduv = random.randint(0, len(targetString) - 1) #finding a random gene to replace
    mutatedGene = random.choice(genes)
    return individual[:indexOfMutatedInduv] + mutatedGene + individual[indexOfMutatedInduv + 1:]

def showStats(bestPerformersList, averageFitnessList, medianFitnessList):
    generationsBest, fitnessBest = zip(*bestPerformersList)
    generationsAvg, fitnessAvg = zip(*averageFitnessList)
    generationsMedian, fitnessMedian = zip(*medianFitnessList)

    plt.plot(generationsBest, fitnessBest, label='Best performer')
    plt.plot(generationsAvg, fitnessAvg, label='Average fitness')
    plt.plot(generationsMedian, fitnessMedian, label='Median performer')

    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.title('Comparing best performer, average fitness, and median performer')
    plt.legend()
    plt.show()


def showChildFitness(childFitnessList):
    generations, childFitnessScores = zip(*childFitnessList)

    plt.plot(generations, childFitnessScores, label='Child Fitness')

    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.title('Child Fitness for every generation')
    plt.legend()
    plt.show()


# Initialize the population
population = [generateIndividual() for _ in range(sizeOfPopulation)]

# Evolution loop
generation = 0
while True:
    # Calculating the fitness for each individual and puts them in a list
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

    bestPerformers.append([generation, bestFitness])
    averageFitness.append([generation, sum(allFitnessScores) / len(allFitnessScores)])
    medianFitness.append([generation, np.median(allFitnessScores)])

    # Ending the while-loop if the program found the solution
    if bestFit == targetString:
        print("The solution is found!")
        showChildFitness(childFitness)
        showStats(bestPerformers, averageFitness, medianFitness)
        break



    #creating new induviduals for the population
    # Select parents based on fitness the fitness scores of the population
    # The parents with the best fitness will have the biggest chanse to get selected
    parents = random.choices(population, weights=allFitnessScores, k=2)

    # Perform crossover and mutation to create new individuals
    child = crossoverUniform(parents[0], parents[1])
    child = mutate(child)


    #Collectiong information about fitness of every child
    childFitness.append([generation, calculateFitness(child)])

    # Replace the least fit individual in the population with the new child
    leastFitIndex = allFitnessScores.index(min(allFitnessScores))
    population[leastFitIndex] = child




    # counter
    generation += 1

    # -> next iteration