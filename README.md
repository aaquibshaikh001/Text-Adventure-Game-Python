# 🧙‍♂️ Text-Based Adventure Game in Python

This is a **console-based interactive text adventure game** developed in Python. Players navigate through a storyline by making choices, collecting items, and encountering branching paths with different outcomes. Designed using core Python features like loops, conditionals, functions, and optional enhancements like inventory persistence, logging, and GUI.

---

## 🚀 Features

- 🗺️ Multiple story paths and outcomes based on player decisions
- 🎒 Basic **inventory management** (e.g., collect, use, or drop items)
- ⛔ Decision consequences (e.g., choose wrong → restart or game over)
- 🧠 Modular game logic using Python functions and conditions
- 📑 Optional logging of decisions, paths taken, and end results
- 🗃️ Optional database (SQLite) support to save game progress
- 🖼️ Optional GUI using `Tkinter` for visual storytelling and inputs

---

## 💻 Technologies Used

- **Python 3**
- `os`, `random`, `time`, `logging` (standard libraries)
- `tkinter` (optional GUI)
- `sqlite3` (optional persistent save system)
- `pandas` (optional reporting/analytics)

---

## 📂 File Structure

📁 Text-Adventure-Game-Python/
├── game.py # Main console game logic
├── story.py # Storyline and decision logic
├── inventory.py # Inventory and item management
├── database.py # SQLite save/load (optional)
├── gui_app.py # Optional Tkinter-based UI
├── logs/ # Folder to store logs
│ └── game.log
├── saves/ # Folder for save files
├── README.md # Project documentation
└── requirements.txt # List of dependencies

yaml
Copy
Edit

---

## 🕹️ How to Play

### 🔹 Console Version:
```bash
python game.py
🔸 GUI Version (optional):
bash
Copy
Edit
python gui_app.py
🧪 Example Gameplay (Console)
text
Copy
Edit
You find yourself in a dark forest. There are two paths ahead.
1. Take the path to the left
2. Enter the cave to the right

> 1

You encounter a wounded traveler. Do you:
1. Help him
2. Ignore and continue

> 1
He gives you a magical amulet! (added to inventory)
📊 Optional: SQLite Save System
sql
Copy
Edit
CREATE TABLE game_state (
    id INTEGER PRIMARY KEY,
    player_name TEXT,
    current_scene TEXT,
    inventory TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
✅ Checklist
 Interactive storyline with branching logic

 Console-based user input/output

 Modular code using functions

 Inventory system

 Error handling for invalid inputs

 GUI using Tkinter (optional)

 Save system using SQLite (optional)

 Logs and reports using logging and pandas (optional)

📈 Future Improvements
Add combat and health system

Include sound effects and background music

Expand to fantasy worlds and maps

Web version using Flask or Django

📄 License
This project is open-source under the MIT License.

✍️ Author
Aaquib Shaikh
GitHub: aaqibshaikh001
