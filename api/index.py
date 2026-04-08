import sys
import os

# Fix import path
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, BASE_DIR)

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from env import DeliveryEnv
from agent import SimpleAgent

app = FastAPI()

# ✅ Correct static path
STATIC_DIR = os.path.join(BASE_DIR, "public")

# Serve static files at /static
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Serve index.html manually at "/"
@app.get("/")
def home():
    return FileResponse(os.path.join(STATIC_DIR, "index.html"))

# Create environment + agent
env = DeliveryEnv()
agent = SimpleAgent()


# 🔄 Reset
@app.get("/reset")
def reset():
    return {"state": env.reset()}


# 🎮 Manual step
@app.get("/step/{action}")
def step(action: int):
    try:
        state, reward, done = env.step(action)
        return {"state": state, "reward": reward, "done": done}
    except Exception as e:
        return {"error": str(e)}


# 🤖 AI step
@app.get("/auto")
def auto():
    try:
        action = agent.choose_action(env.state())
        state, reward, done = env.step(action)
        return {"state": state, "reward": reward, "done": done}
    except Exception as e:
        return {"error": str(e)}


# 🧪 Test route
@app.get("/test")
def test():
    return {"status": "working"}