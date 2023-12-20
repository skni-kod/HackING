import numpy as np

class RLAgent:
    def __init__(self, labirynth_matrix, start_coord, finish_coord, epsilon, gamma, alpha):
        # parametry uczenia
        self.Qtable = np.zeros(17, 17)
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

        # dane labiryntu
        self.finish_coord = finish_coord
        self.start_coord = start_coord
        self.labirynth_matrix = labirynth_matrix

    def choose_action(self, state):
        # eksploracja
        if np.random.rand() < self.epsilon:
            action = np.random.choice(4)
            # eksploatacja
        else:
            action = np.argmax(self.Qtable[state, :])
        return action

    def measure_reward(self, new_state):
        # jezeli ten stan jest sciana
        if self.labirynth_matrix[new_state] == 1:
            return -1
        # jezeli ten stan jest koncem
        elif new_state == self.finish_coord:
            return 1
        # zadne z powyzszych
        else:
            return 0

    def update_Qtable(self, state, action, reward, new_state):
        self.Qtable[state, action] = (1 - self.alpha) * self.Qtable[state, action] \
                                     + self.alpha * (reward + self.gamma * np.max(self.Qtable[new_state, :]))

