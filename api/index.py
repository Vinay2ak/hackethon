import sys
import os
from pathlib import Path

# Fix import path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from env import DeliveryEnv
from agent import SimpleAgent

app = FastAPI()

# Create environment + agent
env = DeliveryEnv()
agent = SimpleAgent()


# 🏠 Serve UI
@app.get("/", response_class=HTMLResponse)
def home():
    try:
        BASE_DIR = Path(__file__).resolve().parent.parent
        file_path = BASE_DIR / "public" / "index.html"
        return file_path.read_text(encoding="utf-8")   # ✅ FIXED HERE
    except Exception as e:
        return f"ERROR: {str(e)}"


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