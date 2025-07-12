# 🏘️ Property Searcher using Breadth-First Search (BFS)

This project is a simple simulation of a **property search system** using the **Breadth-First Search (BFS)** algorithm. It allows users to search for properties in Phnom Penh based on their preferences, such as location, price, and type, by navigating through a graph structure that mimics real-world data.

---

## 📌 Overview

- **Goal:** Demonstrate how BFS can be applied in a real-life scenario like property searching.
- **Approach:** Represent properties and their attributes as nodes and edges in a graph.
- **Language & Tools:** Python, Tkinter (for UI), BFS algorithm.

---

## 🎯 Features

- Simulated property dataset in a graph structure.
- Users can input:
  - Desired location (district in Phnom Penh)
  - Price range
  - Property type (e.g., house, condo, apartment)
- The system finds and displays matching properties using BFS traversal.
- Simple and interactive GUI using Tkinter.

---

## 🧠 How BFS is Used

- The properties are connected in a graph structure.
- BFS starts from a selected node and visits all neighbors layer by layer.
- Properties that meet the user's criteria are selected and shown.

---

## 🚀 Getting Started

### Requirements
- Python 3.x
- Tkinter (usually included with Python)
- sudo apt-get install python3-tk (If TKinter not yet install)

### Installation & Run

```bash
git clone https://github.com/venchiheng/playground.git
cd playground
python main.py
