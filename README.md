
# ✂️ Rock Paper Scissors (RPS) in Python

A simple **console-based Rock Paper Scissors game** written in Python.  
Play against the AI and see who scores more wins!  
Built with only Python’s standard library — no extra dependencies required.

---
<!--
## 🎥 Live Demo

![RPS Demo](demo.gif)

👉 Try it online: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/username/repo/blob/main/rock-paper-scissors.py)
-->

## 🎮 How to Play

- Enter your move as prompted:
  - `r` → Rock  
  - `p` → Paper  
  - `s` → Scissors
- The AI randomly chooses a move.
- The winner of each round is displayed along with the scoreboard.

---

## ▶️ Running the Game

1. Clone this repository:
   ```
   git clone https://github.com/soumyacodes13/repo.git
   cd repo
   ```
3. Run the Python script:
   ```
   python rock_paper_scissors.py
   ```
---

## 📝 Example Gameplay

```
Player enter your move(r/p/s): r

AI choice: scissors
Player choice: rock

Player wins!
- - - - -
|AI count- 0|
-------------
|P count- 1|
- - - - -
```
---

## ⚙️ Requirements

- Python 3.x  
- No external libraries needed (uses only built-in modules)

---

## 📌 Features

- Random AI choice each round  
- Real-time scoreboard  
- Simple console-based interface  
- Works on Linux, macOS, and Windows  

---

## 🚀 Future Improvements (Ideas)

- Add **input validation** for invalid moves
- Limit game to a **certain number of rounds**
- Add a **GUI version** with Tkinter or Pygame
- Add **sound effects** for moves and results

---

## 🧑‍💻 Author

Developed by [Soumyajit](https://github.com/soumyacodes13)

---

## 📜 Source Code
```python
# Rock Paper Scissors
import random
import re

# class rps:
a_count=0
p_count=0
arr={"r":"rock","p":"paper","s":"scissors"}
# def r_p_s()
def ai_choice(arr):
    ch=random.choice(list(arr.keys()))
    return ch


def checkwin(a,p):
    if a[0].lower()==p[0].lower():
        print("AI choice: "+a+" Player choice: "+p)
        print("Draw!")
        return 0
    if a[0].lower()=="r" and p[0].lower()=="p":
        print("AI choice: "+a+" Player choice: "+p)
    elif a[0].lower()=="p" and p[0].lower()=="s":
        print("AI choice: "+a+" Player choice: "+p)
    elif a[0].lower()=="s" and p[0].lower()=="r":
        print("AI choice: "+a+" Player choice: "+p)
    else:
        print("AI choice: "+a+" Player choice: "+p)
        print("AI wins")
        # a_count+=1
        return "ai"
    return "player"
        
def scoreboard(a,p):
    print("- - - - -")
    print("|AI count-",a,"|")
    print("-------------")
    print("|P count-",p,"|")
    print("- - - - -")

while True:
    move=input("Player enter your move(r/p/s): ")
    # if move.lower() not in arr:
    #     print("Invalid input")
    #     break
    s = checkwin(ai_choice(arr), move)
    if s=="ai":
        a_count+=1
    elif s=="player":
        p_count+=1
    scoreboard(a_count,p_count)
