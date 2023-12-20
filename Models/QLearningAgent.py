class QLearningAgent:
    def __init__(self, labirynth):
        self.labirynth = labirynth
        self.q_values = {}
        self.alpha = 0.1
        self.gamma = 0.9
        self.epsilon = 0.1

    def get_q_value(self, state, action):
        return self.q_values.get((state, action), 0.0)

    def update_q_value(self, state, action, reward, next_state):
        current_q = self.get_q_value(state, action)
        best_next_q = max([self.get_q_value(next_state, a) for a in self.get_legal_actions(next_state)])
        new_q = current_q + self.alpha * (reward + self.gamma * best_next_q - current_q)
        self.q_values[(state, action)] = new_q

    def get_legal_actions(self, state):
        x, y = state
        legal_actions = []

        if self.labirynth.is_valid_move((x, y - 1)):
            legal_actions.append("Up")

        if self.labirynth.is_valid_move((x, y + 1)):
            legal_actions.append("Down")

        if self.labirynth.is_valid_move((x - 1, y)):
            legal_actions.append("Left")

        if self.labirynth.is_valid_move((x + 1, y)):
            legal_actions.append("Right")

        return legal_actions


    def choose_action(self, state):
        legal_actions = self.get_legal_actions(state)

        if legal_actions:
            return max(legal_actions, key=lambda a: self.get_q_value(state, a))
        else:
            return "Up"


    def train(self, labirynth, num_episodes=1000):
        for episode in range(num_episodes):
            current_position = labirynth.start_position
            while not labirynth.is_exit(current_position):
                action = self.choose_action(current_position)
                new_position = labirynth.get_new_position(current_position, action)
                reward = labirynth.calculate_reward(new_position)
                self.update_q_value(current_position, action, reward, new_position)
                current_position = new_position