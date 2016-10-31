# import bge
import mathutils
import random
import math

class Neuron():
    def __init__(self, numInputs):

        def weights(numInputs):
            vecWeights = []
            for weight in range(numInputs):
                vecWeights.append(random.random())

            return vecWeights

        self.numInputs = numInputs #number of inputs

        self.vecWeights = weights(numInputs + 1) # vector containing the weights +1 for the bias

class Layer():
    def __init__(self,NumNeurons,NumInputsPerNeurons):

        def createLayer(NumNeurons, NumInputsPerNeuron):
            vecNeurons = []
            for neuron in range(NumNeurons):
                vecNeurons.append(Neuron(NumInputsPerNeuron))
            return vecNeurons



        self.NumNeurons = NumNeurons #number of neurons in the layer
        self.vecNeurons = createLayer(NumNeurons,NumInputsPerNeurons) #list of neurons in the layer

class NeuralNet():

    #__NumInputs = None  # contains the number of inputs
    #__NumOutputs = None  # contains the number of outputs
    #__NumHiddenLayers = None  # contains the number of hidden layers
    #__NeuronsPerHiddenLyr = None  # contains the number of neurons in the hidden layer
    #__vecLayers = None  # list of layers of neurons

    def __init__(self):
        self.__NumInputs = 4 #contains the number of inputs
        self.__Bias = -1 #bias
        self.__NumOutputs = 3 #contains the number of outputs
        self.__NumHiddenLayers = 1 #contains the number of hidden layers
        self.__NeuronsPerHiddenLyr = 6 #contains the number of neurons in the hidden layer
        self.__vecLayers = [] #list of layers of neurons
        self.__ActivationResponse = 1

    def CreateNet(self):
        if self.__NumInputs > 0:
            self.__vecLayers.append(Layer(self.__NeuronsPerHiddenLyr, self.__NumInputs)) # Create Input layer
            for numlayer in range(self.__NumHiddenLayers -1):
                self.__vecLayers.append(Layer(self.__NeuronsPerHiddenLyr, self.__NeuronsPerHiddenLyr)) # Create hidden layers if any
            self.__vecLayers.append(Layer(self.__NumOutputs, self.__NeuronsPerHiddenLyr)) # Create output layer
        else:
            self.__vecLayers.append(Layer(self.__NumOutputs, self.__NumInputs)) #if no hidden layers, create output layer



    def GetWeights(self):
        weights = []
        for layer in self.__vecLayers:
            for neuron in layer.vecNeurons:
                for weight in neuron.vecWeights:
                    weights.append(weight)

        return weights




    def GetNumberOfWeights(self):
        weights = 0
        for layer in self.__vecLayers:
            for neuron in layer.vecNeurons:
                for weight in neuron.vecWeights:
                    weights += 1

        return weights

    def PutWeights(self,vecweights):
        weights = 0
        for layer in self.__vecLayers:
            for neuron in layer.vecNeurons:
                for weight in neuron.vecWeights:
                    weight = vecweights[weights]
                    weights += 1

        return

    def sigmoid(self, netinput, response):
        return (1 / (1 + math.exp(- netinput / response)))

    def Update(self, inputs):
        outputs = []
        cWeight = 0

        if len(inputs) != self.__NumInputs:
            return outputs
        for layer in self.__vecLayers:
            if self.__vecLayers.index(layer) > 0:
                inputs = outputs
            outputs = []
            cWeight = 0
            for neuron in layer.vecNeurons:

                netinput = 0
                for weight in neuron.vecWeights[:-1]:
                    netinput += weight * inputs[cWeight]
                    cWeight += 1
                netinput += neuron.vecWeights[-1] * self.__Bias

                outputs.append(self.sigmoid(netinput, self.__ActivationResponse))
                cWeight = 0
        return outputs











