class DeliveryEnv:
    def __init__(self, level="easy"):
        self.level = level
        self.set_difficulty()
        self.reset()

    def set_difficulty(self):
        if self.level == "easy":
            self.goal = 2
        elif self.level == "medium":
            self.goal = 8
        else:
            self.goal = 18

    def reset(self):
        self.position = 0
        self.steps = 0
        return self.state()

    def state(self):
        return {
            "position": self.position,
            "goal": self.goal
        }

    def step(self, action):
        # action: 0 = left, 1 = right
        if action == 1:
            self.position += 1
        elif action == 0:
            self.position -= 1

        self.steps += 1

        done = False
        reward = -0.1

        if self.position == self.goal:
            reward = 1
            done = True

        return self.state(), reward, done