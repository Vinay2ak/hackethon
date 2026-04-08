import sys
import os
from pathlib import Path

# Fix import path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse

from env import DeliveryEnv
from agent import SimpleAgent

app = FastAPI()

# Create environment + agent
env = DeliveryEnv()
agent = SimpleAgent()


# 🏠 Serve UI
@app.get("/", response_class=HTMLResponse)
def home():
    file_path = Path("public/index.html")
    return file_path.read_text()


# 🔄 Reset
@app.get("/reset")
def reset():
    return env.reset()


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
    except:
        return {"error": "invalid action"}


# 🤖 AI step
@app.get("/auto")
def auto():
    action = agent.choose_action(env.state())
    state, reward, done = env.step(action)
    return {
        "state": state,
        "reward": reward,
        "done": done
    }