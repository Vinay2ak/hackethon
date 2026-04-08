import sys
import os

# Fix import path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from env import DeliveryEnv
from agent import SimpleAgent

app = FastAPI()

# ✅ Serve frontend (IMPORTANT FIX)
app.mount("/", StaticFiles(directory="public", html=True), name="static")

# Create environment + agent
env = DeliveryEnv()
agent = SimpleAgent()


# 🔄 Reset
@app.get("/reset")
def reset():
    result = env.reset()
    return {"state": result}


# 🎮 Manual step
@app.get("/step/{action}")
def step(action: int):
    try:
        state, reward, done = env.step(action)
        return {
            "state": state,
            "reward": reward,
            "done": done
        }
    except Exception as e:
        return {"error": str(e)}


# 🤖 AI step
@app.get("/auto")
def auto():
    try:
        action = agent.choose_action(env.state())
        state, reward, done = env.step(action)
        return {
            "state": state,
            "reward": reward,
            "done": done
        }
    except Exception as e:
        return {"error": str(e)}


# 🧪 Test route
@app.get("/test")
def test():
    return {"status": "working"}