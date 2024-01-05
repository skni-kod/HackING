import math
import numpy as np
from collections import Counter

data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


class Layer:
    def __init__(self, n_inputs, n_neurons, startXY=data[1][1]):  # wielkosc tablicy podanej oraz ilosc neuronow
        self.output = None
        self.startXY = startXY
        self.biases = np.zeros((1, n_neurons))
        self.weights = 0.1 * np.random.randn(n_inputs, n_neurons)  # losowe wagi w zależności od ilości wejść i neuronów
        self.expected_outputs = [[1, 0, 0, 0],
                                 [0, 1, 0, 0],
                                 [0, 0, 1, 0],
                                 [0, 0, 0, 1]]

    def sigmoid_activation_func(self, weighted_sum):
        exp = math.e
        return 1 / (1 + exp ** (-weighted_sum))

    def forward_propagation(self, inputs):
        # bierzemy sume wazona
        wieghted_sum = np.dot(inputs, self.weights) + self.biases
        # w zaleznosci od wyniku aktywujemy neuron
        self.output = self.sigmoid_activation_func(weighted_sum=wieghted_sum)

    def softmax(self, last_layer_input):
        exp_values = np.exp(last_layer_input - np.max(last_layer_input, axis=1, keepdims=True))
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        return probabilities

    def mean_squared_error(self):
        error = np.sum((self.output - self.expected_outputs) ** 2) / (2 * len(self.expected_outputs))
        return error

    def choose_action(self):
        choose_index = []
        for lista in self.output:
            index = -1
            for i in range(len(lista)-1):
                if(lista[i] > lista[i+1]):
                    index = i
            choose_index.append(index)
        return choose_index

    def make_move(self):
        move_index = max(Counter(self.choose_action()), key=Counter(self.choose_action()).get)
        if move_index == 0:
            print("lewo")
        if move_index == 1:
            print("prawo")
        if move_index == 2:
            print("góra")
        if move_index == 3:
            print("dół")

        return move_index

    def backward_propagation(self):
        pass


layer1 = Layer(len(data[0]), 17)
layer1.forward_propagation(data)
layer2 = Layer(len(layer1.output), 4)
layer2.forward_propagation(layer1.output)
layer2.softmax(layer2.output)

print(layer2.output)
print(layer2.choose_action())
print(layer2.make_move())

