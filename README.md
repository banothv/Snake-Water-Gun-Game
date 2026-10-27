# Snake, Water, Gun Game 🐍💧🔫

A simple, interactive command-line game built using Python. Play the classic Snake, Water, Gun game against the computer and test your luck!

## 📌 Project Overview

The Snake, Water, Gun Game is a beginner-friendly Python project that demonstrates fundamental programming concepts such as conditional statements, loops, user input, and random selection.

The player chooses Snake, Water, or Gun, and the computer randomly selects its own choice. The program compares both choices and displays the result.

## ✨ Features

- Interactive command-line gameplay
- Random computer choices
- Win, lose, and draw detection
- Input validation for incorrect choices
- Case-insensitive input support
- Continuous gameplay until the player quits
- Simple and beginner-friendly Python code

## 🛠️ Technologies Used

- **Programming Language:** Python 3
- **Module:** Python `random` module
- **Code Editor:** Visual Studio Code

## 🎮 Game Rules

| Choice | Beats |
|---|---|
| Snake 🐍 | Water 💧 |
| Water 💧 | Gun 🔫 |
| Gun 🔫 | Snake 🐍 |

If both the player and the computer select the same choice, the round ends in a draw.

## 📂 Project Structure

```text
Snake-Water-Gun-Game/
│
├── snake_water_gun.py
└── README.md
```

## ⚙️ Installation and Setup

### 1. Install Python

Download Python from [python.org](https://www.python.org/downloads/) if it is not already installed.

During installation on Windows, enable **Add Python to PATH** if that option is shown.

### 2. Clone the Repository

Open your terminal and run:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### 3. Open the Project Folder

```bash
cd Snake-Water-Gun-Game
```

### 4. Run the Game

```bash
python snake_water_gun.py
```

On Windows, you can also use:

```bash
py snake_water_gun.py
```

## 🕹️ How to Play

1. Run the Python program.
2. Enter `snake`, `water`, or `gun`.
3. View the computer's randomly selected choice.
4. Check the result to see whether you win, lose, or draw.
5. Continue playing as many rounds as you like.
6. Type `quit` to exit the game.

## 🧪 Testing

The game can be tested with the following inputs:

| Test Case | Input | Expected Behavior |
|---|---|---|
| Valid choice | `snake` | Processes the round |
| Valid choice | `water` | Processes the round |
| Valid choice | `gun` | Processes the round |
| Invalid choice | `hello` | Displays an error message |
| Uppercase input | `SNAKE` | Accepts the choice |
| Exit command | `quit` | Ends the game |

## 📚 Concepts Learned

- Python variables and lists
- User input using `input()`
- Conditional statements (`if`, `elif`, `else`)
- Loops using `while`
- Random selection using `random.choice()`
- Input validation
- String methods such as `lower()` and `strip()`

## 🚀 Future Improvements

- Add a player score and computer score
- Display the total number of rounds played
- Add a graphical user interface
- Create a best-of-five game mode

## 👨‍💻 Author

**Banoth Venkatesh**

- GitHub: [banothv](https://github.com/banothv)
- LinkedIn: [Banoth Venkatesh](https://www.linkedin.com/in/banoth-venkatesh-97a584298/)

## 📄 License

This project is available for educational and personal learning purposes. A formal open-source license can be added if the project is intended for redistribution.
