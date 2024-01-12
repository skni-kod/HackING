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
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


class Layer:
    def __init__(self, n_inputs, n_neurons):  # wielkosc tablicy podanej oraz ilosc neuronow
        self.output = None
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
            for i in range(len(lista) - 1):
                if lista[i] > lista[i + 1]:
                    index = i
            choose_index.append(index)
        return choose_index

    def sigmoid_derative(self, x):
        return x * (1 - x)

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

    def backward_propagation(self, learning_rate):
        """
        TODO:
            1) oblicz gradienty dla funkcji kosztu (MSE)
            2) Aktualizuj wagi dla warstwy wyjściowej
            3) Propagacja wsteczna dla warstw ukrytych(jeżeli istnieją)
            4) Aktualizuj wagi dla warst ukrytych
        """
        # 1 gradienty:
        output_err = np.array(self.choose_action()) - np.array(self.expected_outputs)
        output_delta = output_err * self.sigmoid_derative(self.output)

        # 2 wagi i biasy:
        self.weights -= learning_rate * np.dot(self.output.T, output_delta)
        self.biases -= learning_rate * np.sum(output_delta, axis=0, keepdims=True)

        # 3 propagacja wsteczna:
        hidden_err = np.dot(output_delta, self.weights.T)
        hidden_delta = hidden_err * self.sigmoid_derative(self.output)

        # 4:
        self.weights -= learning_rate * np.dot(self.output.T, hidden_delta)
        self.biases -= learning_rate * np.sum(hidden_delta, axis=0, keepdims=True)

    def learning_loop(self, epochs, learning_rate):
        for epoch in range(epochs):
            self.forward_propagation(data)
            self.backward_propagation(learning_rate=learning_rate)
            if epoch % 10 == 0:
                error = self.mean_squared_error()
                print(f'Epoch: {epoch} , Błąd: {error}\n')


layer1 = Layer(len(data), 17)
layer1.learning_loop(epochs=100, learning_rate=0.1)
