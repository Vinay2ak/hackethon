# 🚗 Delivery Agent Environment

## 📌 Description
This project simulates a real-world delivery task where an AI agent must reach a goal position efficiently.

## 🎯 Objective
Move the agent from start (0) to goal position.

## 🎮 Actions
- 0 → Move Left
- 1 → Move Right

## 👀 State
- position
- goal

## 🍬 Reward
- +1 → Reached goal
- -0.1 → Each step

## 🎚️ Difficulty
- Easy → goal = 3
- Medium → goal = 5
- Hard → goal = 10

## ▶️ Run
```bash
python test.py