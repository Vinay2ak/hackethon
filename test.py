from env import DeliveryEnv
from agent import SimpleAgent

def run(level):
    env = DeliveryEnv(level)
    agent = SimpleAgent()

    state = env.reset()
    total_reward = 0

    for _ in range(20):
        action = agent.choose_action(state)
        state, reward, done = env.step(action)
        total_reward += reward

        if done:
            break

    score = max(0, 1 - env.steps / 20)

    print(f"Level: {level}")
    print(f"Steps: {env.steps}")
    print(f"Score: {round(score, 2)}")
    print("-" * 20)


if __name__ == "__main__":
    for level in ["easy", "medium", "hard"]:
        run(level)