# NutriFruit Quiz

A Python application for learning about fruit nutrition through an interactive quiz game.

## Overview

NutriFruit Quiz consists of two main components:

1. **Admin Module**: A command-line interface for managing a database of fruits and their nutritional information.
2. **Quiz Game**: A GUI application that tests knowledge about comparative nutrition values of different fruits.

## Features

### Admin Module (`Admin.py`)
- Add new fruits with nutritional data (calories, fiber, sugar, potassium)
- List all fruits in the database
- Search for specific fruits
- View detailed nutritional information
- Delete entries from the database
- Data persistence using JSON file storage

### Quiz Game (`Fruit_Quiz.py`)
- Interactive GUI built with tkinter
- Randomly generated questions comparing nutritional values
- Score tracking
- User-friendly feedback for correct/incorrect answers

## Screenshots

[Screenshots would be added here]

## Requirements

- Python 3.x
- tkinter (usually comes with Python installation)

## Installation

1. Clone this repository:
```
git clone https://github.com/yourusername/nutrifruit-quiz.git
cd nutrifruit-quiz
```

2. Make sure you have Python and tkinter installed.

## Usage

### Admin Module

Run the admin module to manage your fruit database:

```
python Admin.py
```

Commands:
- `a`: Add a new fruit
- `l`: List all fruits
- `s`: Search for fruits
- `v`: View detailed information about a fruit
- `d`: Delete a fruit
- `q`: Quit the program

### Quiz Game

After adding at least two fruits to your database, run the quiz:

```
python Fruit_Quiz.py
```

- Click on the fruit you believe has the higher value for the displayed nutritional component
- Your score will be tracked as you play

## How It Works

The application uses a JSON file (`data.txt`) to store fruit data. The admin module manages this database, while the quiz game reads from it to generate questions. Each fruit entry includes values for energy (calories), fiber, sugar, and potassium content per 100g.

## Project Structure

```
nutrifruit-quiz/
├── Admin.py          # Command-line admin interface
├── Fruit_Quiz.py     # GUI quiz game
├── data.txt          # JSON database (generated on first run)
└── README.md         # This file
```

## Future Improvements

- Add more nutritional components (vitamins, minerals, etc.)
- Implement difficulty levels
- Add graphical representations of nutritional data
- Create a web-based version
- Add user accounts and high scores

## Author

Zameel
