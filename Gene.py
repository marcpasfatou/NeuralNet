import math
import random


class Chromosome():

    def __init__(self):
        self.vecWeights = []
        self.Fitness = 99999


class GenAlg():

    def __init__(self, popsize, MutRat,CrossRat,numweights):
        self.__vecPop = [] #list of chromosomes
        self.__PopSize = popsize #number of chromosomes
        self.__ChrLen = numweights
        self.__TotFit = 0
        self.__avgFit = 0
        self.__maxFit = 0
        self.__minFit = 99999
        self.__bestGen = 0
        self.__mutRate = MutRat
        self.__crossRate = CrossRat
        self.__numGen = 0
        self.__Perturbation = 0.2
        self.__numCopies = 5
        self.__numBest = 4

        for i in range(self.__PopSize):
            self.__vecPop.append(Chromosome())
            for chromosome in range(self.__ChrLen):
                self.__vecPop[i].vecWeights.append(random.random())


    def crossover(self, mum, dad, baby1,baby2):

        if random.random() > self.__crossRate or mum == dad:
            baby1 = mum
            baby2 = dad
            return

        chiasma = random.randint(0,len(self.__ChrLen - 1))

        for i in range(chiasma):
            baby1.vecWeights.append(mum.vecWeights[i])
            baby2.vecWeights.append(dad.vecWeights[i])
        for i in range(chiasma,self.__ChrLen):
            baby1.vecWeights.append(dad.vecWeights[i])
            baby2.vecWeights.append(mum.vecWeights[i])


    def mutation(self, chr):
        for gene in chr.vecWeights:
            if random.random() < self.__mutRate:
                gene = random.random()*self.__Perturbation


    def getchrRoulette(self):

        slice = random.random()*self.__TotFit
        currentFit = 0
        for i in self.__vecPop:
            currentFit += i.Fitness
            if currentFit >= slice:
                return i



    def grabnbest(self,NBest, NumCopies, vecPop):
         while NBest:
             for i in range(NumCopies):
                 vecPop.append(self.__vecPop[-NBest])
             NBest -= 1



    def CalculateBestWorstAvTot(self):
        self.__TotFit = 0

        currentHigh = 0
        currentLow = 999999

        for chromosome in self.__vecPop:
            if chromosome.Fitness > currentHigh:
                currentHigh = chromosome.Fitness
                self.__bestGen =  self.__vecPop.index(chromosome)
                self.__maxFit = currentHigh
            if chromosome.Fitness < currentLow:
                currentLow = chromosome.Fitness
                self.__minFit = currentLow




    def reset(self):
        self.__TotFit = 0
        self.__maxFit = 0
        self.__minFit = 99999
        self.__bestGen = 0

    def epoch(self, oldPop):
        self.__vecPop = oldPop
        self.reset()
        print("pop",self.__vecPop)
        self.__vecPop.sort(key = lambda chr: chr.Fitness)
        self.CalculateBestWorstAvTot()

        vecNewPop = []

        if not self.__numCopies * self.__numBest % 2:
            self.grabnbest(self.__numBest, self.__numCopies,vecNewPop)

        while len(vecNewPop) < self.__PopSize:
            mum = self.getchrRoulette()
            dad = self.getchrRoulette()
            baby1 = Chromosome()
            baby2 = Chromosome()

            self.crossover(mum,dad, baby1, baby2)

            self.mutation(baby1)
            self.mutation(baby2)

            vecNewPop.append(baby1)
            vecNewPop.append(baby2)
        self.__vecPop = vecNewPop
        return  self.__vecPop

    













