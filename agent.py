import random

class SimpleAgent:
    def choose_action(self, state):
        # Always move toward goal
        if state["position"] < state["goal"]:
            return 1  # move right
        else:
            return 0  # move left