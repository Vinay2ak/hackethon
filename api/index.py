import sys
import os

# Fix import path (so env.py is found)
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from pathlib import Path
from env import DeliveryEnv
from agent import SimpleAgent

# Create environment + agent
env = DeliveryEnv()
agent = SimpleAgent()


class handler(BaseHTTPRequestHandler):
    def do_GET(self):

        # 🏠 Serve UI
        if self.path == "/":
            file_path = Path("public/index.html")
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(file_path.read_bytes())
            return

        # 🔄 Reset
        elif self.path == "/reset":
            response = env.reset()

        # 🎮 Manual step
        elif self.path.startswith("/step"):
            try:
                action = int(self.path.split("/")[-1])
                state, reward, done = env.step(action)
                response = {
                    "state": state,
                    "reward": reward,
                    "done": done
                }
            except:
                response = {"error": "invalid action"}

        # 🤖 AI step
        elif self.path == "/auto":
            action = agent.choose_action(env.state())
            state, reward, done = env.step(action)
            response = {
                "state": state,
                "reward": reward,
                "done": done
            }

        # ❌ Unknown route
        else:
            response = {"error": "route not found"}

        # Send JSON response
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())


# 🚀 START SERVER
if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), handler)
    print("Server running on http://localhost:8000")
    server.serve_forever()